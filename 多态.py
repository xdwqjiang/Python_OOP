class Animal:
    def jiao(self):
        pass

class Dog(Animal):
    def jiao(self):
        print("汪汪汪")

class Cat(Animal):
    def jiao(self):
        print("喵喵喵")

def test(obj): # python不关注传过来的obj对象的格式，而是只关心obj是否存在下述的方法，如果存在，则正常执行
    obj.jiao()

d = Dog()
c = Cat()
test(d)