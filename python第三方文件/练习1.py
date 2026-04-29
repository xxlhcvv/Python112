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
