class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        pass
    def __str__(self):
        # 信息格式化，如果不进行信息格式化的话，print(实例)输出的是地址信息，而非我们想要的信息，而通过这种信息格式化可以使得输出我们想要的信息
        # 理解：应该是print该实例时会自动调用__str__函数
        return "这个人的姓名是：%s，这个人的年龄为：%s"%(self.name, self.age)
    pass
p1 = Person("s", 18)
print(p1.age, p1.name)
print(p1)
# 获取该字符串
s = str(p1)
print(s, type(s))

# 由于使用了__str__函数进行了信息格式化，导致无法看到实例的内存信息，此时可以用repr函数来获取本质信息
print(repr(p1))

# __call__：使得”对象“具备当作函数来调用的能力，例如：p1=Person(),此时实例p1不能通过"p1()"调用
class Person1:
    pass
p = Person1()
# p() # TypeError: 'Person1' object is not callable

class Person2:
    def __call__(self, *args, **kwargs):
        # 表示对于不加名称的参数传给args(元组)，对于增加名称的参数传输给kwargs(字典)
        print("xxx", args, kwargs)
    pass
pp = Person2()
pp(1, 2, name="jiang")

# ----------------__call__函数的使用场景----------------
# 创建很多个画笔（画笔的类型（钢笔，铅笔），画笔的颜色（红，黄，蓝，绿））
print("创建了一个%s这个类型的画笔，它是%s颜色"%("钢笔", "红色"))
# 如果说每次都写一个这样的输出命令，会使得代码非常的复杂，并且观察不难发现，画笔的种类是要少于画笔颜色的，利用__call__方法实现简单调用
class PenFactory:
    def __init__(self, p_type):
        self.p_type = p_type
        pass
    def __call__(self, p_color):
        print("创建了一个%s这个类型的画笔，它是%s颜色"%(self.p_type, p_color))
        pass
    pass

gangbiF = PenFactory("钢笔") # 创建了gangbiF实例，这个实例可以通过函数调用的方式直接调用__call__函数
qianbiF = PenFactory("铅笔")
gangbiF("绿色")
gangbiF("红色")
qianbiF("蓝色")

