#对象
#创建对象
#类的专有方法__init__,在实例化对象时自动运行
#删除对象
#类的专有方法__init__,释放对象时被调用
class cat:
    '''模拟猫'''
    #构造方法__init__  ,创建对象时自动运行
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    #析构方法__del__ ，删除对象时自动运行
    def __del__(self):
        print('--析构函数被调用')
    # 普通方法
    def sleep(self):
        return '%d岁的%s正在沙发上睡觉。' % (self.__age, self.__name)
    def eat(self, food):
        self.food = food
        return '%d岁的%s正在吃%s。' % (self.__age, self.__name, self.food)
#实例化对象时自动调用构造方法__init__,传入名字和年龄
new_cat=cat('Tom',3)
print(new_cat.sleep())
print(new_cat.eat('小鱼干'))
cat2=cat('小咪',5)
print(cat2.eat('猫粮'))
print(new_cat)
cat3=cat('candy',8)
#删除对象cat3
del cat3
#print(cat3)
#对象属性
print(cat2.name,cat2.age)
#对象属性的私有化，不能单独访问数据属性
#在属性前面添加双下画线，在类内部使用属性是也要有双下画线


class car:
    def __init__(self, newWheelNum, newColor):
        self.newWheelNum = newWheelNum
        self.newColor = newColor
    def run (self):
        print("车在跑，目标:夏威夷。")
    def __del__(self):
        print("---析构方法被调用---")
BMW=car(4,"黑色")
print('车轮数:%d,颜色:%s'%(BMW.newWheelNum,BMW.newColor))
BMW.run()