class car:
    wheel = 4
    color = 'red'

    def getcarlnfo(self, name):
        return '%s有%d个轮子，颜色是%s' % (name, car.wheel, car.color)

    def run(self):
        return "车行驶在学习的大道上"


new_car = car()
print(new_car.getcarlnfo("奔驰"))
print(new_car.run())
