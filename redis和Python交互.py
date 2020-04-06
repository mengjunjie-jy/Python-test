from redis import *

if __name__ == "__main__":
    try:
        # 创建StrictRedis对象，与redis服务器建⽴连接
        sr = StrictRedis()
        # 添加键name，值为itheima
        result = sr.set('d', 'itheima')
        # 输出响应结果，如果添加成功则返回True，否则返回False
        print(result)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        # 创建StrictRedis对象，与redis服务器建⽴连接
        sr = StrictRedis()
        # 获取键name的值
        result = sr.get('d')
        # 输出键的值，如果键不存在则返回None
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        # 创建StrictRedis对象，与redis服务器建⽴连接
        sr = StrictRedis()
        # 设置键name的值，如果键已经存在则进⾏修改，如果键不存在则进⾏添加
        result = sr.set('d', 'itcast')
        # 输出响应结果，如果操作成功则返回True，否则返回False
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        # 创建StrictRedis对象，与redis服务器建⽴连接
        sr = StrictRedis()
        # 设置键name的值，如果键已经存在则进⾏修改，如果键不存在则进⾏添加
        result = sr.delete('d')
        # 输出响应结果，如果删除成功则返回受影响的键数，否则则返回0
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        # 创建StrictRedis对象，与redis服务器建⽴连接
        sr = StrictRedis()
        # 获取所有的键
        result = sr.keys()
        # 输出响应结果，所有的键构成⼀个列表，如果没有键则返回空列表
        print(result)
        for i in iter(result):
            print(i.decode())
    except Exception as e:
        print(e)
