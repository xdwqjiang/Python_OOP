# 2.只读属性：一个属性(一般指的是实例属性)，只能读取，不能写入
# 方式1(1)：先全部隐藏(将属性进行私有化，使其既不能读也不能写)，然后进行部分公开（通过实例化方法）
class Person:
    def __init__(self):
        self.__age = 18 # 私有属性，既不能读也不能写
        pass
    # 定义公开方法
    def getAge(self):
        return self.__age
    pass
p1 = Person()
print(p1.getAge())

# 方式1(2)：使用@property装饰器
class Person1:
    def __init__(self):
        self.__age = 18
        pass
    # 主要作用是，可以使用属性的方式，来调用这个方法
    @property
    def age(self):
        return self.__age
    pass
# 这种定义只读属性的方式，不仅能够只读属性，而且当对实例创建相同名字的属性时，程序会报错，而非像第一种定义的方式在实例中增加该属性
p2 = Person1()
print(p2.age) # 实际上这里的age调用的不是属性，而是age这个方法，只是形式上时调用属性的形式


# 方式2：系统内置方法
class Person2:
    def __init__(self):
        self.age = 10
        pass
    # __setattr__函数：当我们通过 实例.属性=值 给一个实例增加一个属性，或者是修改一下属性的值的时候，都会调用这个方法
    # 在这个方法内部才会真正的将这个 属性 和 值 给存储到__dict__字典里面
    # 所以为了构建只读属性，要对这个存储函数进行修改，具体的方法是：1.先判断属性的名称是否是只读的属性，这个属性是否已经存在
    # 2.如果说这个属性不是只读属性的名称，就将它加入到这个实例中去
    def __setattr__(self, key, value):
        # 1.判定，key，是否是我们要设置的只读属性的名称，并且判断实例和类中是否存在该属性
        if key == "age" and key in self.__dict__.keys():
            print("这是个只读属性，不能设置数据")
        else:
            # 2.如果说这个属性不是只读属性的名称，就将它加入到这个实例中去
            # self.key = value # 不能用这种方式赋值，因为一旦涉及到对实例增加属性或者修改属性的值就会调用这个__setattr__函数，然后陷入无限次的循环中
            self.__dict__[key] = value # 用这种直接在字典中修改的方式就会避免调用__setattr__这个命令
            pass
        pass
    pass

M = Person2()
M.age = 19
M.name = 'jiang'
print(M.age)
print(M.__dict__)
