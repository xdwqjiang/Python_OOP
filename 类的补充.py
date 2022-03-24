# python的元类是type类，其余所有的类对象都可以看做是从元类中实例化出来的
num = 10 # 是一个对象
s = 'abc' # 是一个对象
print(num.__class__)
print(s.__class__)
print(num.__class__.__class__)
print(s.__class__.__class__)

class Person:
    pass
p = Person()
print(p.__class__)
print(p.__class__.__class__)
print(p.__class__.__class__.__class__)

# ----------类的创建方法-----------------
# 用type创建类（通过元类来创建）
# 符号说明：xxx是指向Dog类的变量，程序中通过xxx来调用Dog类，Dog是类的名称
def run():
    print("----")
    pass
xxx = type("Dog",(),{"count":10, "run":run}) # 通过定义键值对来给类增加属性和方法
xxx.run()

# --------------类的创建流程-----------
# 创建流程是：先查看自己定义的类中是否指明了元类，如果没有指明，去父类中寻找元类，
# 如果父类中也没有指明元类，则会去模块中寻找是否指明了元类，如果模块中没有指明元类，则采用默认的type类来创建类对象
# 总结：先判断有没有自定义的元类，如果没有的话就调用系统的元类type来创建类对象

# __metaclass__ = xxx # 在模块中指明元类
class Animal:
    # __metaclass__ == xxx # 在父类中指明元类
    pass

class Person(Animal): # 继承Animal类，也可以说Animal类是Person的父类
    # __metaclass__ == xxx # 通过__metaclass__指明类的元类为xxx
    pass
