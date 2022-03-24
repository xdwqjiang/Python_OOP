# 定义三个类：小狗、小猫、人
# 小狗：姓名，年龄(默认为1) 吃饭、玩、睡觉、看家(格式：名字是xx,年龄xx岁的小狗在xx)
# 小猫：姓名，年龄(默认为1) 吃饭、玩、睡觉、捉老鼠(格式：名字是xx,年龄xx岁的小猫在xx)
# 人：姓名，年龄(默认为1)，宠物  吃饭、睡觉、玩(格式：名字是xx,年龄xx岁的人在xx)
#                           养宠物(让所有的宠物，吃饭、睡觉、玩)
#                           让宠物工作(让宠物根据自己的职责进行工作)

# 首先根据三个类的公有的属性和行为，定义一个Animal的父类，让其他三个类继承Animal中的父类的资源
class Animal:
    def __init__(self, name, age=1): # 默认值为1，注意一般来说有默认值的参数一般放在最后，以避免参数的错位
        self.name = name
        self.age =age

    def eat(self):
        print("%s吃饭" % self)

    def sleep(self):
        print("%s睡觉" % self)

    def play(self):
        print("%s玩耍" % self)

class Dog(Animal):

    def work(self):
        print('%s看家' % self)

    def __str__(self):
        return "名字是{},年龄{}的小狗在".format(self.name, self.age)
class Cat(Animal):

    def work(self):
        print('%s捉老鼠' % self)

    def __str__(self):
        return "名字是{},年龄{}的小猫在".format(self.name, self.age)

class Person(Animal):
    def __init__(self, pets, name, age):
        super().__init__(name, age)
        self.pets = pets

    def KeepPets(self):
        print("%s在养宠物" % self)
        for pet in self.pets:
            pet.eat()
            pet.sleep()
            pet.play()


    def MakePetWork(self):
        for pet in self.pets:
            pet.work("%s在让宠物工作" % self)

    def __str__(self):
        return "名字是{}，年龄为{}的人在".format(self.name, self.age)

dog = Dog("xz",18)
c = Cat("kadi", 18)
p = Person([c, dog], 'sz', 1) # 注意的是这里输入的实例必须是可遍历的类型，所以定义的是实例的列表
p.KeepPets()
