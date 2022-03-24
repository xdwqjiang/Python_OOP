# 1.定义一个类
class Person:
    pass

# 2.根据类，创建一个对象
P = Person()

# 3.给对象增加属性
P.age = 18

# 4.验证是否有添加成功
print(P.age)

# python自带__dict__来查看对象的所有属性
P.height = 180
print(P.__dict__)

# print(P.sex)
# AttributeError: 'Person' object has no attribute 'sex'，定义的对象中没有sex这个属性

P.pets = ["小花", "小黑"] # 中括号是列表
P.pets.append("小黄") # 对对象中的pets属性的列表增加“小黄”这一元素,列表是一个可变类型
print(P.pets)

# 删除一个对象的属性
num = 10
del num # 删除变量
# print(num)
del P.age # 删除了对象P中的age
print(P.__dict__)

# --------------类属性的操作-----------------
print("类属性的操作")
class MoneyTest1:
    pass

# 给类增加属性
# 方式1：将类看作是一个对象进行处理
MoneyTest1.count = 1 # 对类增加count属性
print(MoneyTest1.count)
print(MoneyTest1.__dict__)
# 方式2：直接在类里面定义属性
class MoneyTest2:
    age = 18
    num = 666
    pass
print(MoneyTest2.__dict__)

one = MoneyTest1()
# 更改对象的类
print(one.__class__)
one.__class__ = MoneyTest2
print(one.__class__)

# 访问一个对象的属性，如果对象中存在该属性，则输出对象的属性值，如果对象中没有对该对象，则程序会输出类中的属性值
one.age = 10
print(one.age) # 输出对象的属性值
print(one.num) # 输出类中的属性值

# 如何修改一个类的属性
# 方法：通过类名进行修改，如果属性存在则是修改属性的值，如果属性不存在，则是对类增加属性
MoneyTest2.age = 22
print(MoneyTest2.age)

# 如何删除一个类的属性：通过类名进行删除，注意不能通过对象属性的删除对类中的属性进行查询
del MoneyTest2.age
print(MoneyTest2.__dict__)

one1 = MoneyTest2()
one1.__dict__ = {"name": "jiang"} # 通过增加键值对的方式增加对象的属性
# 在创建对象时，会给对象创建一个__dict__的属性，指向的是类属性的字典，对对象的__dict__增加键值对，相当于对对象增加属性
# 注意只能修改对象中的__dict__属性，类中的__dict__属性是只读的，默认情况下是不能修改的，后面可以通过某些函数可以对类中的__dict__属性进行修改
print(one1.name)

one.age = 18
# 对象中的__dict__属性是可以进行修改的
one.__dict__["age"] = 20
print(one.age)

# 类的属性被各个对象共享，当类中的属性被修改，对应的对象的属性也会被修改
one = MoneyTest2()
two = MoneyTest2()
print(one.num, two.num)
MoneyTest2.num = 10
print(one.num, two.num)

# 限定对象可以增加的属性
class Person:
    __slots__ = ["age"] # 限制对象只能增加age的属性，此时类中没有__dict__属性
    pass
p1 = Person()
p1.age = 9
p1.num = 10
print(p1.age)

