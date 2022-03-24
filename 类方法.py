class Person:
    @classmethod
    def leifangfa(cls):
        print("这是一个类方法", cls)
        pass
    pass

# 1.通过类方法进行调用
Person.leifangfa()

# 2.通过实例调用
p = Person()
p.leifangfa() # 传递的不是p这个实例，传递的是p的类Person

# 如果用衍生类进行调用类方法，则传回的参数是衍生类
class A(Person):
    pass
A.leifangfa()

