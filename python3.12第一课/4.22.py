#面向对象编程
#类，对现实事务的抽象，使用class定义
class cat:
    '''模拟猫咪'''
    #属性
    name= 'tom'
    age=3
    #方法
    def sleep(self):
        return '%d岁的%s正在睡觉'%(self.age,self.name)
    def eat(self,food):
        self.food=food
        return '%d岁的%s正在吃%s'%(self.age,self.name,self.food)
#实例化对象
cat1=cat()
print(cat1)
print(cat1.sleep())
print(cat1.eat('小鱼干'))


class daqiao:
    '''模拟英雄大乔'''
    #属性
    name = '大乔'
    role = '辅助'

    #方法：英雄的技能
    def skill_1(self):
        return '%s释放一技能鲤跃之潮，对路径敌人造成伤害并推开' % self.name

    def skill_3(self):
        return '%s开启三技能水之愈,在指定位置召唤法阵传送队友回城并立刻满血' % self.name

    def skill_4(self):
        return '%s说：“守望着天空，大海，和你的回忆,并召唤队友' % self.name


#实例化对象
daqiao1 = daqiao()
print(daqiao1)
print(daqiao1.skill_1())
print(daqiao1.skill_3())
print(daqiao1.skill_4())


'''创建一个Car类，代表一辆汽车，具有车轮数（4）和颜色（red）的属性，
以及两个函数：getCarInfo和run。通过实例化Car类并调用其方法，可以
看到汽车的基本信息和行驶状态。'''

# （1）使用class语句创建Car类，添加车轮数和颜色两个属性。
class Car:
    wheelNum = 4
    color = 'red'

    # （2）使用def关键字定义getCarInfo函数，增加参数name，返回名字、
    # 车轮数和颜色3个属性的字符串。
    def getCarInfo(self,name):
        self.name = name
        return '%s有%d个车轮，颜色是%s。'%(self.name,self.wheelNum,self.color)

    # （3）使用def关键字定义run函数，返回语句“车行驶在学习的大道上。”。
    def run(self):
        return '车行驶在学习的大道上。'

# （4）调用Car类赋值于new_car。
new_car = Car()

# （5）使用new_car调用getCarInfo函数和run函数。
print(new_car.getCarInfo('小车'))
print(new_car.run())