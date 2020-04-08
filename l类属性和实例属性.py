class People(object):
    country = 'china'  # 类属性


print(People.country)
People.country = 'ls'
p = People()
print(p.country)
p.country = 'japan'
print(p.country)  # 实例属性会屏蔽掉同名的类属性
print(People.country)
del p.country  # 删除实例属性
print(p.country)

"""
总结：
    如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。
如果通过实例对象去引用，会产生一个同名的实例属性，这种方式修改的
是实例属性，不会影响到类属性，并且之后如果通过实例对象去引用该名
称的属性，实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删
除了该实例属性。
"""
