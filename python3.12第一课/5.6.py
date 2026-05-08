# 类的继承
class Cat:
    def __init__(self):
        self.name = '猫'
        self.age = 4
        self.info = [self.name, self.age]
        self.index = -1
    def run(self):
        return f"{self.name}--在跑"
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def __iter__(self):
        print("名字 年龄")
        return self
    def next(self):
        if self.index == len(self.info) - 1:
            raise StopIteration
        self.index += 1
        return self.info[self.index]

class Bosi(Cat):  # 子类波斯猫继承猫类
    def setName(self, newname):
        self.name = newname
    def eat(self):
        return f"{self.name}--在吃"

# 创建对象
bs = Bosi()
print(bs.name, bs.age)  # 子类继承了父类的属性
print(bs.run())  # 子类继承了父类的方法
bs.setName('波斯猫')
print(bs.name)  #子类的属性和方法
print(bs.eat())
# 迭代输出父类的属性
iterator = iter(bs.next, 1)
for info in iterator:
    print(info)


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

class Land_Rover(Car):
    def __init__(self, brand, color, wheel_num, turbo):
        super().__init__(brand, color)
        self.wheel_num = wheel_num
        self.turbo = turbo

Luxury_car = Land_Rover("Land Rover", "白色", 4, True)
print("车辆颜色：", Luxury_car.color)

attrs = list(Luxury_car.__dict__.keys())
attr_iter = iter(attrs)
print("\n对象属性迭代输出：")
for attr in attr_iter:
    print(f"{attr}: {getattr(Luxury_car, attr)}")