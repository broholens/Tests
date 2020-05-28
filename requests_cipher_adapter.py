"""
requests指定加密协议及加密套件

参考链接：
python官方文档：https://docs.python.org/3/library/ssl.html#cipher-selection
openssl ciphers：https://www.python.org/dev/peps/pep-0543/#openssl
requests配置TLS：https://lukasa.co.uk/2017/02/Configuring_TLS_With_Requests/
加解密算法写法说明：https://zhuanlan.zhihu.com/p/37239435
Python安全：https://python-security.readthedocs.io/ssl.html
代码样例：https://www.programcreek.com/python/example/106815/ssl.PROTOCOL_TLSv1_2
CERTIFICATE_VERIFY_FAILED：https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error
"""

import ssl

import requests
from requests.adapters import HTTPAdapter


class TLS12Adapter(HTTPAdapter):
    """使用加密协议TLS1.2及以上和加密套件访问https链接"""
    # 暂时不校验证书, 设置为ssl.CERT_NONE
    CERT = ssl.CERT_NONE
    # 指定TLS协议
    PROTOCOL = ssl.PROTOCOL_TLS
    # 加密套件 参考https://www.python.org/dev/peps/pep-0543/#openssl
    CIPHERS = ':'.join((
        "ECDHE+AESGCM",
        "DHE+AESGCM"
    ))

    def init_poolmanager(self, *args, **kwargs):
        kwargs['ssl_context'] = self._create_context()
        return super(TLS12Adapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        kwargs['ssl_context'] = self._create_context()
        return super(TLS12Adapter, self).proxy_manager_for(*args, **kwargs)

    def _create_context(self):
        context = ssl._create_unverified_context(protocol=self.PROTOCOL, cert_reqs=self.CERT)
        # 仅支持TLS1.2及以上协议
        context.options |= ssl.OP_NO_TLSv1
        context.options |= ssl.OP_NO_TLSv1_1
        context.options |= ssl.OP_NO_COMPRESSION
        context.set_ciphers(self.CIPHERS)
        return context
    

class RequestsClient:
    def __init__(self):
        self._session = None
        
    @property
    def session(self):
        if not self._session:
            self._session = requests.session()
            # 对所有https://开头的请求都使用Adapter
            self._session.mount('https://', TLS12Adapter())
        return self._session
