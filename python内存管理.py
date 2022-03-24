# 可以通过id()函数获取内存地址(10进制)
# 可以通过hex()函数获取对应的16位内存地址
class Person:
    pass

p = Person()
print(p)
print('实例存放的地址(10进制)：%d'%id(p))
print('实例存放的地址(16进制)：%s'%hex(id(p)))

# 对于整数和短小的字符，python会对其进行缓存，不会创建多个相同的对象
num1 = 2
num2 = 2
print(id(num1), id(num2)) # 我们可以发现num1和num2都指向同一个地址单元
# 容器对象，存储其他对象，仅仅是其他对象的引用，并不是其他对象本身，就比如p = Person()，这个p并不是对象本身，而是存储的是指向这个对象的地址

# --------引用计数器------------
# 通过sys.getrefcount()函数来查看引用次数
import sys
class Person2:
    pass

p1 = Person2()
p2 = p1 # 这里使得p2和p1都指向同一个实例，也就是说实例被引用了2次
# 可以通过sys.getrefcount()函数来查看引用次数
print(sys.getrefcount(p1)) # 这里得到的引用数比实际的引用数+1原因是用实参去初始化形参的时候，引用被复制了

del p2
print(sys.getrefcount(p1))

# -------------引用计数器机制-特殊场景-循环引用问题---------------
# 内存管理机制
# 当一个对象，如果被引用 +1 删除一个引用 -1 如果等于0则自动被释放
# 循环引用（会造成内存空间无法释放，内存泄露）
import objgraph
# python3使用objgraph包来绘制引用关系
class Person3:
    pass
class Dog:
    pass
p = Person3()
d = Dog()
p.dog = d
d.per = p
print(objgraph.count("Person3"))
print(objgraph.count("Dog"))
print(sys.getrefcount(p))
del p
del d
print(objgraph.count("Person3"))
print(objgraph.count("Dog"))

# 垃圾回收机制：分代回收
# 垃圾回收器中，新增的对象个数-消亡的对象个数，达到一定的阈值时，才会触发垃圾检测(通过gc模块进行查看)
import gc

print(gc.get_threshold()) # 输出是一个元组 (700, 10, 10) 700是阈值，只有当新增对象个数-消亡对象个数大于700时，触发垃圾检测
# 第一个10代表当0代被检测10次的时候才会触发1次0，1代检测，第二个10代表当1代被检测了10次的时候会触发一次0，1，2代检测

# 这些参数可以通过gc.set_threshold()函数进行设置
gc.set_threshold(200, 10, 10)

# 垃圾回收机制：需要注意的是垃圾检测特别的费事费力
# 1.自动回收：
# (1)开启垃圾回收机制(默认是开的) 开启 gc.enable() 关闭 gc.disable() 判断是否开启 gc.isenabled()
# (2)达到了垃圾回收机制的阈值
# 2.手动回收

print(gc.isenabled())
gc.disable()
print(gc.isenabled())

# 手动回收，并且解决循环引用的问题

class Person4:
    pass
class Dog4:
    pass
p4 = Person4()
d4 = Dog4()
p4.dog = d4 # 让两个实例对象相互引用，产生循环引用
d4.per = p4
del p4
del d4
# 由于存在循环引用，导致内存没有释放
print(objgraph.count("Person4"))
print(objgraph.count("Dog4"))
# 可以同gc.collect()函数来处理垃圾，如果不设置参数，认为处理所有的垃圾
gc.collect()
print(objgraph.count("Person4"))
print(objgraph.count("Dog4"))