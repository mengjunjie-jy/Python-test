# 定义父类
class Father:
    def cure(self):
        print("父亲给病人治病...")


# 定义子类继承父类
class Son(Father):
    # 重写父类中的方法
    def cure(self):
        print("儿子给病人治病...")


# 定义函数,在里面 调用 医生的cure函数
def call_cure(doctor):
    # 调用医生治病的方法
    doctor.cure()


# 创建父类对象
father = Father()
# 调用函数,把父类对象传递函数
call_cure(father)

# 创建子类对象
son = Son()
# 调用函数,把子类对象传递函数
call_cure(son)


"""
多态的好处:
​ 给call_cure(doctor)函数传递哪个对象,在它里面就会调用哪个对象的cure()方法,
也就是说在它里面既可以调用son对象的cure()方法,也能调用father对象的cure()方法,
当然了也可以在它里面调用Father类其它子类对象的cure()方法,这样可以让call_cure(doctor)
函数变得更加灵活,额外增加了它的功能,提高了它的扩展性.
"""
