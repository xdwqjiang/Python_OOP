class Person:
    age = 0 # 类属性
    pass

p = Person()
p.num = 10 # 实例属性

# 类属性可以通过类进行访问，也可以通过实例进行访问
print(Person.age)
print(p.age)

# 实例属性，只能通过实例来访问实例属性，不能通过类来找到实例的属性
print(p.num)

