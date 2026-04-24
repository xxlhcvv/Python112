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

