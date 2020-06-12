# python fake
fake提供伪造数据，包括但不限于手机号、地址、user-agent、isbn、身份证号(ssn)、信用卡信息、文章段落<br>
具体可以参考[官方文档](https://faker.readthedocs.io/en/stable/providers.html#)

### fake实现逻辑
- fake含有很多providers，每个provider用于提供一类fake数据。<br>
- fake支持多种语言，所以每类fake数据均有多种不同语言的provider类。<br>
- 调用时首先通过proxy.py解析locale，支持在初始化时指定多个locale，然后将其他参数映射到factory.py生成fake对象，映射过程中会通过指定/默认locale加载指定/全部的providers。<br>
- 每类fake数据都会提供一个Provider类(继承自BaseProvider)，这个Provider类提供本类数据的操作方法(如address类的city方法)，
- 每种语言都会继承此Provider类，数据均来自于每种语言的__init__.py中。<br><br>

### 示例
- 基本示例
```python
>>> from faker import Faker
>>> fake = Faker(locale="zh_CN")
>>> fake.name_female()
'石红'
>>> fake.name_male()
'郭飞'
>>> fake.phone_number()
'13273633376'
>>> fake.safe_email()
'kzhu@example.net'
>>> fake.sentence()
'是否孩子事情公司解决.'
```
- 创建自己的provider
```python
from faker import Faker
fake = Faker()

# first, import a similar Provider or use the default one
from faker.providers import BaseProvider

# create new provider class
class MyProvider(BaseProvider):
    def foo(self):
        return 'bar'

# then add new provider to faker instance
fake.add_provider(MyProvider)

# now you can use:
fake.foo()
# 'bar'
```
- 使用指定单词创建sentence
```python
from faker import Faker
fake = Faker()

my_word_list = [
'danish','cheesecake','sugar',
'Lollipop','wafer','Gummies',
'sesame','Jelly','beans',
'pie','bar','Ice','oat' ]

fake.sentence()
# 'Expedita at beatae voluptatibus nulla omnis.'

fake.sentence(ext_word_list=my_word_list)
# 'Oat beans oat Lollipop bar cheesecake.'
```
