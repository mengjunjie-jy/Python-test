import json

a = '帅哥'
print(type(a))  # <class 'str'> 字符串默认编码utf-8，字符类型为str，存储类型为unicode数据
print(json.dumps(a))  # "\u5e05\u54e5"

b = a.encode()  # 默认为utf-8，将字符串a编码为b，字符类型为bytes，存储类型为字节类型
print(type(b))  # <class 'bytes'>
print(b)  # b'\xe5\xb8\x85\xe5\x93\xa5'

c = b.decode()  # 按照utf-8编码将字符串b解码，字符类型为str，存储类型为unicode数据
print(type(c))  # <class 'str'>
print(c)  # 帅哥
print(json.dumps(c))  # "\u5e05\u54e5"
