import random
import time

def get_qingkuang():
    qingkuang_list=[
        "今天心情很好",
        "今天有点疲惫",
        "今天非常开心",
        "今天平平淡淡",
        "今天充满希望",
        "今天学要休息",
        "今天适合学习",
        "今天适合放松",
    ]
    return random.choice(qingkuang_list)

def get_tianqi():
    tianqi_list=[
        "晴天",
        "阴天",
        "微风",
        "温暖",
        "清爽",
        "多云",
        "阳光充足",
        "很长舒适"
    ]
    return random.choice(tianqi_list)

def get_zhufu():
    zhufu_list=[
        "愿你每天都快乐",
        "愿你学习顺利",
        "愿你万事顺心",
        "愿你平安健康",
        "愿你好运常在",
        "愿你努力有回报",
        "愿你生活很美好",
        "愿你天天都开心",
    ]
    return random.choice(zhufu_list)

def show_jieguo():
    print("正在为你生成今日状态")
    time.sleep(1)
    print("生成中")
    time.sleep(1)
    print("生成完成")
    time.sleep(1)

    print("")
    print("=========")
    print("今日心情")
    print(get_qingkuang())
    print("")
    print("今日天气")
    print(get_tianqi())
    print("")
    print("今日祝福")
    print(get_zhufu())
    print("=========")
    print("")

def main():
    print("欢迎使用心情情报系统")
    print("本程序可以随机生成你的心情和祝福")
    print("")
    name=input("请输入你的名字:")
    print("")
    print("你好",name)
    print("马上为你播报")
    print("")

    show_jieguo()

    print("感谢使用心情播报系统")
    print("希望你每天都开心")

if __name__=="__main__":
    main()



