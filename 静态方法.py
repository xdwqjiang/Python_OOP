class Person:
    @staticmethod
    def jingtai():
        print("这是一个静态方法")
        pass
    pass
# 类调用
Person.jingtai()

# 实例调用
p =Person()
p.jingtai()
