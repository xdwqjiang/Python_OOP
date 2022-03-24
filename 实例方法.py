class Person:
    def eat(self, food):
        print("在吃饭", food)
        pass
    pass

# 实例方法的调用
# 1.使用实例调用（标准调用），这种调用方式自动的将实例传递到实例函数中的self中去
p = Person()
p.eat("土豆")

# 2.使用类调用（不推荐）
Person.eat(p, "黄瓜")

# 3.间接调用（不推荐）
func = Person.eat # 将eat这个实例方法赋给func这个变量
func(p, "西瓜")
