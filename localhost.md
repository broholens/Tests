# 127.0.0.1、localhost、0.0.0.0

### 127.0.0.1
属于环回地址，环回地址：所有发往该类地址的数据包都应该被loop back。<br>
使用这个地址发送数据，则数据包不会出现在网络传输过程中。
#### 用途
- 测试某台机器上的网络设备，操作系统或者TCP/IP实现是否工作正常：ping 127.0.0.1

### 0.0.0.0
- 在服务器中，0.0.0.0指的是本机上的所有IPV4地址
- 在路由中，0.0.0.0表示的是默认路由，即当路由表中没有找到完全匹配的路由的时候所对应的路由。
#### 用途
- 如果主机有大小网两个IP，且主机上一个服务监听的地址为0.0.0.0，则两个IP均可访问该服务。

### localhost
域名。默认指向127.0.0.1
