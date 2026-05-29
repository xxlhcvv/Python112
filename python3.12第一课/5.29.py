# 代码9-4
from test_paper import Test_Paper
# 抽取试卷
total = Test_Paper.learning_coin()  # 调用函数，获取学习币
print('学习币值为：', total)
topics = Test_Paper.rule(total)  # 调用函数，抽取试卷
print('------- 试卷抽取完毕 -------')
print('试卷内容为：', topics)

# 代码9-5
print('\n------- 测试开始 -------')
new_name = input('请输入姓名：')
nn = 1
while nn > 0:
    if len(new_name) == 0:
        new_name = input('尚未输入，请重新输入名字：')
    else:
        nn = -1
    nn += 1

answers = []  # 定义用于存储答案的列表
tp = 0
try:
    while tp < len(topics):
        # 获取题目
        print('第' + str(tp + 1) + '题：' + ''.join(topics[tp]))
        # 用键盘输入答案
        answer = input('请输入第' + str(tp + 1) + '题的答案（注意输入格式为“正确”或“错误”）：')
        print('\n')
        # 判断输入格式是否正确，正确则进入下一步，否则提示重新输入
        if answer == '正确' or answer == '错误':
            answers.append(answer)
            tp += 1
        else:
            print('输入格式有误，请重新审题并按正确格式作答。\n')
except:
    print(' ')




# 代码9-7
import csv
import os
# 定义函数获取试卷答案：根据学习币值所在范围读取相应的文件
def info_answer(total):
    """..."""
    # 使用os模块查看试卷答案文件夹下的文件名
    print('试卷答案文件为：', '/'.join(os.listdir(r'D:\Python\python3.12第一课\data\学生测试\试卷答案')))
    if 3 <= total <= 10:
        with open(r'D:\Python\python3.12第一课\data\学生测试\试卷答案\A卷答案.csv', 'r',
                  encoding=('UTF-8-sig')) as f:
            a = csv.DictReader(f)
            answer_a = [aa['答案'] for aa in a]
            print('------- 正在获取A卷答案 -------')
        return answer_a
    elif 11 <= total <= 18:
        with open(r'D:\Python\python3.12第一课\data\学生测试\试卷答案\B卷答案.csv', 'r',
                  encoding=('UTF-8-sig')) as f:
            b = csv.DictReader(f)
            answer_b = [bb['答案'] for bb in b]
            print('------- 正在获取B卷答案 -------')
        return answer_b

# 代码9-8
# 调用函数，获得标准答案
original_answers = info_answer(total)
# 计算成绩时，将输入的答案与标准答案进行匹配
# 题目答对时加分，题目答错时不加分也不扣分，每题10分，共10题
print('\n------- 正在计算测试评分 -------\n')
res = 0
for j in range(len(answers)):
    if answers[j] == original_answers[j]:
        res += 10
    else:
        res += 0
print(new_name + '的成绩为：' + str(res))
print('\n标准答案为：', original_answers)