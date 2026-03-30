while True:
    age = input("请输入你家狗狗的年龄：")
    if age.isdecimal():
        age = int(age)
        if age <= 0:
            print("你在逗我吧!")
        elif age == 1:
            print("相当于14岁的人。")
        else:
            human = 22 + (age -2)*5
            print("相当于人类的年龄:", human)
    elif age.upper()=='Q':
        print("计算结束！")
        break
    else:
        print("请输入数字，按Q键退出！")