# 索引操作：可以对一个实例对象进行索引操作（列表或者是字典形式）
# 使用三种内置方法，可以以索引的形式操作对象
# 增/改：p[1] = 666,p['name']='sz'
# 查找：p[1],p['name']
# 删除：del p[1],del p['name']
class Person:
    # 如果不定义以下三个内置函数的话，就不能够通过索引操作来对实例进行操作
    # 补充：如果不需要输出操作，可以直接在__setitem__,__getitem__,__delitem__函数中只写pass即可
    def __setitem__(self, key, value):
        # 代表的是设置一个元素,新增/修改
        print("setitem", key, value)
        pass
    def __getitem__(self, item):
        # 代表的是查找一个元素
        print("getitem", item)
        pass
    def __delitem__(self, key):
        # 代表的是删除一个元素
        print("delitem", key)
        pass
    pass

p = Person()
p["name"] = 'sz' # 此时只是能够说明能够通过索引操作将数据传过去，但是没有进行在实例中保存
print(p.__dict__)

# 接下来通过命令将通过索引操作传过来的参数保存到实例中
class Person1:
    def __init__(self):
        self.cache = {} # 定义一个空字典用来接收数据
    def __setitem__(self, key, value):
        # 代表的是设置一个元素,新增/修改
        print("setitem", key, value)
        self.cache[key] = value # 增加字典
        pass
    def __getitem__(self, item):
        # 代表的是查找一个元素
        print("getitem", item)
        return self.cache[item] # 这里的item也是key的作用
        pass
    def __delitem__(self, key):
        # 代表的是删除一个元素
        print("delitem", key)
        del self.cache[key]
        pass
    pass
p2 = Person1()
p2['name']='jiang'
print(p2.__dict__)
print(p2['name'])
del p2['name']
print(p2.__dict__)


# ----------比较操作（比较两个实例中的某个属性的大小）-----------
# 通过内置函数给定不同两个实例之间的比较规则
class Person3:
    def __init__(self, age, height):
        self.age = age
        self.height = height
        pass
    # 定义等于号
    def __eq__(self, other):
        return self.age == other.age
    # 不等于号
    def __ne__(self, other):
        return self.age != other.age
    # 大于号
    def __gt__(self, other):
        return self.age > other.age
    # 大于等于号
    def __ge__(self, other):
        return self.age >= other.age
    # 小于号
    def __lt__(self, other):
        return self.age < other.age
    def __le__(self, other):
        return self.age <= other.age

pp1 = Person3(18, 180)
pp2 = Person3(19, 180)

# 如果定义了一个比较符，比如是等于号，则解释器会通过调换参数（对调self和other）的方法调用该方法，不用再定义不等于号了
# 大于对应的是小于（注意：并不对应小于等于），大于等于对应小于等于
print(pp1 == pp2)
print(pp1 != pp2)
print(pp1 > pp2)

# -------上下文环境中的布尔值-----
class Per:
    pass
per = Per()
if per: # 非空即True
    print("xxx")

# 通过在类中调用内置函数__bool__来控制返回的布尔值
class Per1:
    def __bool__(self):
        return False # 返回的布尔值
    pass
per1 = Per1()
if per1:
    print("xxx")

# 应用场景，判断是否成年
class Student:
    def __init__(self, name, age):
        self.age = age
        self.name =name
        pass
    def __bool__(self):
        return self.age>=18
    pass

def shifou(x):
    if x:
        print("%s是成年人"%x.name)
    else:
        print("%s不是成年人"%x.name)
stu1 = Student("jiang", 19)
stu2 = Student("xing",17)
shifou(stu1)
shifou(stu2)

# -------遍历操作------------
# 怎样使我们自己创建的实例可以可以使用for in? 不能之际用 for i in p来访问，会报错
# 方法1：实现__getitem__方法
class Pers:
    def __init__(self):
        self.result = 1
        pass

    def __getitem__(self, item):
        self.result += 1
        if self.result >= 5:
            raise StopIteration("停止遍历") # raise指的是抛出的意思，抛出中断遍历的命令
        # 要注意迭代的时候要定义终止条件
        return self.result
    pass
p = Pers()
for i in p:
    print(i)

# 方式2
class Pers1:
    def __init__(self):
        self.result = 1
        pass

    # def __getitem__(self, item):
    #     print("getitem")
    #     self.result += 1
    #     if self.result >= 5:
    #         raise StopIteration("停止遍历") # raise指的是抛出的意思，抛出中断遍历的命令
    #     # 要注意迭代的时候要定义终止条件
    #     return self.result

    # __iter__方法优先级高于__getitem__方法
    def __iter__(self):
        # 该方法要求函数返回迭代器
        self.result = 1 # 每次重新调用迭代器时会恢复迭代器初始值
        # return iter([1, 2, 3]) # 可以通过iter()函数构建迭代器，如果迭代器是与实例有关的话，则需要进一步定义__next__函数
        return self
    def __next__(self):
        self.result += 1
        if self.result >= 5:
            raise StopIteration("停止遍历")
        return self.result
    pass
# 定义了__iter__和__next__的类的实例p是个迭代器
p = Pers1()
# for i in p:
#     print(i)
# print("实例中迭代器的输出（恢复初始值）")
# for i in p:
#     print(i)

print("实例中迭代器的输出")
print(next(p))
print(next(p))

# -------恢复迭代器初始值--------------
# 见代码161行
# 结论：一个对象如果是迭代对象，只需要实现__iter__方法即可，迭代器需要实现__iter__和__next__方法，所以一个迭代器一定是一个迭代对象，而一个迭代对象不一定是一个迭代器



# 迭代器的使用方法
# 通过iter函数构建迭代器，利用迭代器构建循环
l = [1, 2, 2, 3, 5]
l1 = iter(l)
while True:
    try:
        x = next(l1)
        print(x)
    except StopIteration:
        break

# ---------描述器---------
# 可以描述一个属性操作的对象，描述器本身也是一个对象
# 定义方式1：property
class miaoshuqi:
    def __init__(self):
        self.__age = 10
    def get_age(self):
        return self.__age
    def set_age(self, value):
        # 在修改属性值的时候，可以增加数据过滤的条件
        if value < 0:
            print("输入有误")
            value = 0
        self.__age = value
        pass
    def del_age(self):
        del self.__age
        pass
    age = property(get_age, set_age, del_age) # 这里定义了属性age的描述器，通过该描述器可以通过调用属性的方法对属性进行操作
    # 当然这里的property也可以通过修饰器的那种写法进行定义描述器

p = miaoshuqi()
p.age = -1
print(p.age)
del p.age

# --------描述器-定义2-----------
# 按方法1，一个属性的描述器需要定义3个方法，那么3个属性就要定义9个方法，明显不利于编程，用面向对象的思想，将相同的操作放在一起
# 简单来说就是将修改、查找、删除命令定义成一个类，然后在对属性进行实例化这个类
# 注意定义了描述器后一般是用实例（而非类）来进行操作的
class Age(object):
    def __get__(self, instance, owner):
        # 注意，要返回的是这里的instance的属性值
        print("get")
        return instance.v

    def __set__(self, instance, value): # 注意，要修改的是这里的instance的属性值
        print("set")
        instance.v = value

    def __delete__(self, instance):
        print("delete")
        del instance.v
    pass

class miaoshuqi1(object):
    age = Age() # 实例化描述器类
    pass
p = miaoshuqi1()
p.age = 18
print(p.age)
del p.age

# 资料描述器 get set
# 非资料描述器 仅仅实现了get
# 优先级：资料描述器>实例属性>非资料描述器

# ---------使用类，实现装饰器------------
