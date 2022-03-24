# 在类中定义方法
class Person:
    def eat2(self):
        print("这是一个实例方法", self)
        pass
    @classmethod
    def leifangfa(cls): # 修饰器
        print("这是一个类方法", cls)

    @staticmethod
    def jingtaifangfa():
        print("这是一个静态方法")
    pass

p = Person()

p.eat2()
print(p)
# 通过输出我们不难看出类方法接收的第一个参数self是一个实例
p.leifangfa()


# 方法的划分
# 1.实例方法：默认第一个参数需要接收到一个实例
# 2.类方法：默认第一个参数需要接收到一个类
# 3.静态方法：默默的看着前两个装逼，第一个参数啥也不默认接收

# 上述三种方法都存在类里面，没有在实例里面，方法存放在类的__dict__中
print(p.__dict__)
print(Person.__dict__)
