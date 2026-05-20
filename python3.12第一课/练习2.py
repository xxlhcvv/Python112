import random
random_float = random.uniform(0, 100)
random_int = random.randint(0, 100)
gift = ["便捷风扇", "毛绒公仔", "精品牙刷", "保温杯", "空调被", "陶瓷餐具"]
choice = input("请选择猜的类型（输入 1 猜整数 / 输入 2 猜浮点数）：")
if choice == "1":
    guess = int(input("请输入你猜的整数（0~100）："))
    if guess == random_int:
        print(f"🎉 恭喜你猜对了！正确数字是：{random_int}")
        print("🎊 开始抽奖...")
        print(f"你抽到的奖品是：{random.choice(gift)}")
    else:
        print(f"❌ 很遗憾，猜错了，正确数字是：{random_int}")
elif choice == "2":
    guess = float(input("请输入你猜的浮点数（0~100，保留两位小数即可）："))
    # 浮点数判断，保留两位小数比较
    if round(guess, 2) == round(random_float, 2):
        print(f"🎉 恭喜你猜对了！正确数字是：{round(random_float, 2)}")
        print("🎊 开始抽奖...")
        print(f"你抽到的奖品是：{random.choice(gift)}")
    else:
        print(f"❌ 很遗憾，猜错了，正确数字是：{round(random_float, 2)}")
else:
    print("⚠️ 输入无效，请重新运行程序并选择 1 或 2")