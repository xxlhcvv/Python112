import random
import csv
import os


class Test_Paper:
    # 定义learning_coin函数获取学习币
    def learning_coin(numbers=3, points=None):
        '''
        输入
        ----------
        numbers: 骰子个数
        points: 骰子点数

        输出
        ----------
        total: 学习币值
        '''
        points = []
        while numbers > 0:
            point = random.randrange(start=1, stop=7)  # 生成1～6的随机整数
            points.append(point)  # 将生成的随机整数添加到列表中
            numbers = numbers - 1
        total = sum(points)  # 获得的学习币值
        return total  # 返回学习币值

    # 代码9-3
    # 定义划分试卷的规则并抽取试卷
    def rule(total):
        '''
        输入
        ----------
        total: 学习币值

        输出
        ----------
        Volume_A: A卷题目或Volume_B: B卷题目
        '''
        # 使用os模块查看试卷文件夹下的文件名
        print('全部试卷文件有：', '/'.join(os.listdir(r'D:\Python\python3.12第一课\data\学生测试\试卷')))
        if 3 <= total <= 10:  # 学习币值在[3,10]中抽取A卷
            with open(r'D:\Python\python3.12第一课\data\学生测试\试卷\A卷.csv', 'r',
                      encoding=('UTF-8-sig')) as f:
                a = csv.reader(f)
                Volume_A = [aa for aa in a]
                print('-------- 正在抽取A卷 --------')
                return Volume_A
        elif 11 <= total <= 18:  # 学习币值在[11,18]中抽取B卷
            with open(r'D:\Python\python3.12第一课\data\学生测试\试卷\B卷.csv', 'r',
                      encoding=('UTF-8-sig')) as f:
                b = csv.reader(f)
                Volume_B = [bb for bb in b]
                print('-------- 正在抽取B卷 --------')
            return Volume_B

