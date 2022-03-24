class Person:
    """
    这是一个人的类
    """
    age = 19 # 在__init__()外面的属性不需要实例化也能直接修改，这样实例化的默认值也跟着改变
    def __init__(self):
        self.name = "sz"
    def run(self):
        print("run")
        pass
    pass
# __dict__:类的属性及其对应的值
# __bases__:类的所有父类构成元组
# __doc__:类的文档字符串
# __name__:类名
# __module__:类定义所在的模块
# __dict__:实例的属性
# __class__:实例对应的类

# 对类而言
# __dict__:类的属性及其对应的值
print(Person.__dict__)
# __bases__:类的所有父类构成元组
print(Person.__bases__)
# __doc__:类的文档字符串
print(Person.__doc__)
# __name__:类名
print(Person.__name__)
# __module__:类定义所在的模块
print(Person.__module__)

# 对实例而言
p1 = Person()
# __dict__:实例的属性
print(p1.__dict__)
# __class__:实例对应的类
print(p1.__class__)