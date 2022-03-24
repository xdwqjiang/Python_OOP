# 经典类和新式类
# 经典类：没有继承(object)，python2.x版本定义一个类时，默认不继承
# 新式类：继承(object)，python3.x版本定义一个类时，默认继承

class Person:
    pass
print(Person.__bases__) # __bases__查看Person的基类
# 注意：创建类对象的类是元类，子类继承的父类是基类，基类可以看成是元类的实例
# type->object->新式类  type->经典类
