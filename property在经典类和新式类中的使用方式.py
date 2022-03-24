# 第一种使用方法
class Person(object):
    def __init__(self):
        self.__age = 18
    def get_age(self):
        return  self.__age

    def set_age(self, value):
        self.__age = value

    age = property(get_age, set_age) # 此时类中的age属性和get_age以及set_age命令关联起来
    pass
p = Person()
print(p.age)
p.age = 90
print(p.age)

# 第二种使用方法
class Person1(object):
    def __init__(self):
        self.__age = 18
        pass
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
        pass

    @age.deleter
    def age(self):
        del self.__age
        pass
    pass

p2 = Person1()
print(p2.age)
del p2.age # 删除属性


