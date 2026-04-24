class car:
    def __init__(self, newWheelNum, newColor):
        self.newWheelNum = newWheelNum
        self.newColor = newColor
    def run (self):
        print("车在跑，目标:夏威夷。")
    def __del__(self):
        print("---析构方法被调用---")
BMW=car(4,"黑色")
print(f"车轮数：{BMW.newWheelNum}，颜色：{BMW.newColor}")
BMW.run()