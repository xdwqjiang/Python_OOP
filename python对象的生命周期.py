# 生命周期：指的是一个对象从诞生到消亡的过程
# 当一个对象被创建时，会在内存中分配相应的内存空间进行存储
# 当这个对象不在被使用，为了节约内存就会将这个对象释放
class Person:
    # def __new__(cls, *args, **kwargs):
    #     print("新建了一个对象，但是被我拦截了")
    #     pass
    # 对象初始化方法
    def __init__(self):
        print("这是初始化方法")
        self.name = 'jiang'
    def __del__(self):
        print("这个对象被释放了")
p = Person()
print(p)
print(p.name)
# 我们的代码中并没有调用释放对象的程序，但是程序会自动地帮我们释放对象

# ------监听对象生命周期的方法(小案例)----------------
# 要求查看类创建对象的个数（创建一个实例+1，删除一个实例-1）
class Person1:
    # 创建一个私有的类属性，用来记录实例的个数(创建为私有属性的目的：为了使得该元素的值不能轻易的在类外修改)
    __count = 0
    def __init__(self):
        print("计数+1")
        Person1.__count += 1 # 注意，这里不应该是self.__count，而是应该直接在类属性上进行修改，参数共享到所有的实例中
        pass

    def __del__(self):
        print("计数-1")
        pass
    @staticmethod # 说明该方法是静态方法
    def log():
        print('当前的实例个数为%d'%Person1._Person1__count)

p1 = Person1()
Person1.log()
p2 = Person1()
Person1.log()
