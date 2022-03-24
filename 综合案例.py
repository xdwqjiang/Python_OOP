# ---------------综合案例---------------
# 实现一个简单的加法运算器
# 难点：修饰器的使用，修饰器的嵌套，链式编程
import win32com.client # 这个程序是调用win语音的包

class Caculator:
    # 定义一个实例属性，如果定义的是类属性的话，类属性是共享到所有的实例中去的，如果定义的是实例属性，每一个实例相当于一个单独的计算器
    def __init__(self, num):
        self.__result = num # 初始化实例属性，定义为私有属性的原因：使其只能通过实例方法进行操作
        pass
    # 定义播报的函数，以后修改的播报的话只需要在这一个地方修改即可
    def __say(self, word):
        # 1.创建一个播报器对象
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        # 2.通过这个播报器，直接播放对应的语音字符串
        speaker.Speak(word)

    # # 用装饰器来对运算的数据输入做限定(这里用装饰器的优势：1.不需要对函数内部进行修改，2.减少代码的冗余)
    # def __say_zsq(func):
    #     def inner(self, n):
    #         # 1.创建一个播报器对象
    #         speaker = win32com.client.Dispatch("SAPI.SpVoice")
    #         # 2.通过这个播报器，直接播放对应的语音字符串
    #         speaker.Speak(n)
    #         return func(self,n)
    #     return inner
    # 增加一个新的函数，使其能够定义一个修饰器
    def creat_say_zsq(word=''): # 默认空字符串
        def __say_zsq(func):
            def inner(self, n):
                self.__say(word + str(n))
                return func(self, n)
            return inner
        return __say_zsq # 函数返回的是一个装饰器，这样就是能使其根据不同的参数构建不同的修饰器

    def __check_num_zsq(func): # 定义这个方法为私有方法，因为其只在实例使用
        def inner(self, n):
            if not isinstance(n, int):
                raise TypeError("输入数据有误，应为整形数据")
            return func(self, n)
        return inner

    @__check_num_zsq
    @creat_say_zsq("加")       # 注意装饰器的嵌套顺序，应该是先检查数据，然后语音播报
    def jia(self, n):
        self.__result += n
        return self # 这里的运算结束后返回的是实例，因此可以直接继续调用实例方法，这样写的好处是可以写链式
    @__check_num_zsq
    @creat_say_zsq("减去")
    def jian(self, n):
        self.__result -= n
        return self
    @__check_num_zsq
    @creat_say_zsq("乘以")
    def cheng(self, n):
        self.__result *= n
        return self

    def show(self):
        self.__say("计算的结果是：%d"%self.__result)
        print("计算的结果是：%d"%self.__result)
        return self
    def clear(self):
        self.__result = 0
        self.__say("清零")
        return self
    # 最后增加属性访问的方法
    @property
    def result(self):
        return self.__result
    pass

p1 = Caculator(0)
p1.jia(2)
p1.jia(3)
p1.show()
print(p1.result)
# 链式计算
p2 = Caculator(10).jia(5).jian(6).show().clear().jia(5).cheng(10).show()