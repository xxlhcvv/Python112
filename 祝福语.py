import random


def generate_funny_msg():
    #素材库（有趣，接地气）
    subjects = ["你", "我", "我们", '这个世界', 'python', '你的电脑']
    verbs = ['喜欢', '爱上', '依赖', '需要', '守护']
    adjectives = ['超级', '无敌', '可爱', '温暖', '幸运']
    objects = ['每一天', '所有代码', '所有美好', '所有幸运']

    #随机组合
    subj = random.choice(subjects)
    verb = random.choice(verbs)
    adj = random.choice(adjectives)
    obj = random.choice(objects)

    #有趣的结尾版块
    endings = [
        '不信你运行一下代码试试',
        '连编译器都替我喜欢你',
        '这是电脑经过十万次计算后的结果！',
        '跑一次，快乐就生效！'
    ]
    end = random.choice(endings)
    return f"{subj}{verb}{adj}{obj}{end}"


#主程序
if __name__ == "__main__":
    print("===【python专属祝福机】===")
    name = input("输入你的名字：")
    print(f"\n送给{name}的专属祝福:\n")

    #循环生成5条有趣的祝福
    for _ in range(5):
        print(generate_funny_msg())

    print(f"\n运行完这段代码，你的好运已经加载完成！")
