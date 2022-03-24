# 私有化属性的应用场景：1.数据保护、2.数据过滤

class Person:
    # 主要作用：当我们创建好一个实例之后，会自动的调用这个方法来初始化这个对象
    def __init__(self):
        self.age = 18
        self.__agep = 20
        pass

    # 由于私有属性只能在类中进行处理和调用，因此可以在类中定义修改和返回私有属性的方法，后面程序可以通过调用实例方法来修改和得到私有属性的值
    def setAge(self, age):
        if isinstance(age, int) and 0 < age <200:# isinstance(o,t)判断对象o是否是t类型
            self.__agep = age
        else:
            print("input error")
        pass
    def getAge(self):
        return self.__agep
    pass
p1 = Person()
p2 = Person()
print(p1.age)
print(p2.age)

# 数据的保护
p1.setAge(50) # 注意这里只是对实例p1中的隐私属性进行了修改，而不会修改类中的隐私属性，所以对于p2实例而言，其__agep仍未20
print(p1.getAge())
print(p2.getAge())

# 数据的过滤(在类中定义修改隐私属性的函数中增加对数据的判断语句)
p1.setAge(-10)
print(p1.getAge())