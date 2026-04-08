#结合循环语句增加猜数字次数，让自己猜中数字
import random

x = random.randint(0, 100)  #随机生成0~100的数
print(x)
while True:  #一直循环
    y = int(input("请输入数字："))
    if x < y:
        print("大了")
    elif x > y:
        print("小了")
    else:  # y==x
        print("猜对了！")
        break  #结束循环
