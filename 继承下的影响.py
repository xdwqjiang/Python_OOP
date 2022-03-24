# 继承下的影响
# 1.资源的继承：在python中资源的继承指的是资源的使用权，所以测试某个资源能不能被继承，其实就是测试在子类中，能不能访问到父类当中的这个资源

# 2.资源的使用：
# 问题：如果子类和父类具有相同的资源(属性和方法)，那么进行调用的时候调用的是谁的资源
# 针对不同的继承形态(单继承链，无重叠的多继承链，有重叠的多继承链)，访问的顺序是不同的
# 对于单继承而言，从下向上找
# 无重叠的多继承链：单调原则，一条一条继承链的找，先找左侧的链 （深度优先）
# 对于有重叠的多继承链：先在其多个父类中寻找，找不到再在其父类的父类中进行寻找 （广度优先）

# 3.资源的覆盖：优先级高的父类中的定义会覆盖优先级低的父类中的资源
# 比如：假设优先级顺序：A->B->C->D 如果在D类中有一个方法run(),而A，B，C中都没有，然后访问A中的run()方法实际调用的是D中的方法
# 然而，在程序中我们给C增加了一个新的方法，名字为run()，此时通过A访问的run()方法就变成了访问C类的方法，这种现象就称为C中的资源”覆盖“了D中的资源
# 这里的”覆盖“并不是说D中的方法不存在了，只是访问不到C就不继续访问了

# 4.资源的累加：在一个类的基础上增加一些额外的资源，子类相比于父类多一些自己特有的资源

# 1.资源(属性和方法)的继承
class Animal:
    # 设置不同权限(公有、保护、私有)的属性和方法，测试在继承的子类中能否访问到这些资源
    a = 1
    _b = 2
    __c = 3

    def t1(self):
        print("t1")
    def _t2(self):
        print("t2")
    def __t3(self):
        print("t3")
    def __init__(self):
        print("init")

class Person(Animal):
    def test(self):
        print(self.a)
        print(self._b)
        # print(self.__c)
        self.t1()
        self._t2()
        # self.__t3()
        self.__init__()
# 结论：私有的属性和方法不能被继承，公有的、受保护的属性和方法以及内置方法能够被继承
p = Person()
p.test()
Animal.a = 666
p.test()
# 注意：继承的属性和方法只是具有使用权(相当于访问父类原本的存储空间)而非是复制了一份
# 仿真可以看到，我们仅仅对父类的公有属性a进行修改，而子类的访问的属性也是修改后的结果

class B:
    age = 10
class A(B):
    pass
print(A.age)
A.age = 9 # 注意这里的这个命令并不会修改父类B中的age属性，而是会在A这个子类中增加age属性
print(B.age)
print(A.age)

# 2.资源的使用
# 问题：如果子类和父类具有相同的资源(属性和方法)，那么进行调用的时候调用的是谁的资源
# 针对不同的继承形态(单继承链，无重叠的多继承链，有重叠的多继承链)，访问的顺序是不同的(C3算法)
# 对于单继承而言，从下向上找
# 无重叠(无公共父类)的多继承链：单调原则，一条一条继承链的找，先找左侧的链 (深度优先)
# 对于有重叠的多继承链：先在其多个父类中寻找，找不到再在其父类的父类中进行寻找

# 4.资源的累加
# 场景：有一个A继承自B，然后想要在B的属性基础上，增加一些新的A的属性
class B:
    age = 18
    def __init__(self):
        self.height = 100

    def shilifangfa(self):
        print("实例方法")

    @classmethod
    def leifangfa(cls):
        print("类方法")

    @staticmethod
    def jingtaifangfa():
        print("静态方法")

class A(B):
    def __init__(self):
        self.name = "sz"

    def t1(self):
        print("t1")

a = A()
print(a.__dict__) # {'name': 'sz'}我们发现由于在A类中重新定义了__init__函数，所以没有继承B的实例属性
print(a.age) # 但是类属性还是可以访问的

# 使其能够累加：方法1：类名调用，方法2：super()
class B1:
    age = 18
    def __init__(self):
        self.height = 100

    def shilifangfa(self):
        print("实例方法")

    @classmethod
    def leifangfa(cls):
        print("类方法")

    @staticmethod
    def jingtaifangfa():
        print("静态方法")

class A1(B1):
    def __init__(self):
        # 方法1：类名调用
        # B1.__init__(self) # 这里的self指的是下面传上来的实例a1
        # 方法2：super()
        super().__init__() # super()，命令继承的是在访问顺序表中的前一个的类，不一定是父类，比如：菱形结构中A->B->C->D，B继承的是C，而C并不是B的父类
        self.name = "sz"

    def t1(self):
        # 方法1：类名调用
        # B1.shilifangfa(self)
        # 方法2：super()
        super().shilifangfa()
        print("t1")

    @classmethod
    def t2(cls):
        # 方法1：类名调用
        # B1.leifangfa()
        # 方法2：super()
        super().leifangfa()
        print("t2")

    @staticmethod
    def t3():
        # 方法1：类名调用
        B1.jingtaifangfa()
        # super().jingtaifangfa() # 静态方法，静态成员不能使用super()
        print("t3")


a1 = A1()
print(a1.__dict__) # {'name': 'sz'}我们发现由于在A类中重新定义了__init__函数，所以没有继承B的实例属性
a1.t1()
a1.t2()
a1.t3()
