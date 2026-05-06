#生成迭代器
class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.info=[self.name,self.age]
        self.index=-1
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def __iter__(self):#迭代函数
        print('名字,年龄')
        return self
    def next(self):#迭代函数
        if self.index==len(self.info)-1:
            raise StopIteration
        self.index+=1
        return self.info[self.index]
newcat=cat('coffe',3)
print(newcat.getName())
#调用迭代函数
iterator=iter(newcat.next,1)
for info in iterator:
    print(info)


class car:
    def __init__(self, brand, wheelnum, color, T):
        self.brand = brand
        self.wheelnum = wheelnum
        self.color = color
        self.T = T
        self.info = [brand, wheelnum, color, T]
        self.index = -1

    def getBrand(self):
        return self.brand

    def getWheelnum(self):
        return self.wheelnum

    def getNewcolor(self):
        return self.color

    def getT(self):
        return self.T

    def __iter__(self):
        print("品牌 车轮数 颜色 废气涡轮增压")
        return self

    def __next__(self):
        if self.index == len(self.info) - 1:
            raise StopIteration
        self.index += 1
        return self.info[self.index]


newcar = car("奔驰", 4, "白色", True)
print("车辆颜色：", newcar.getNewcolor())
iterator = iter(newcar)
for info in iterator:
    print(info)
