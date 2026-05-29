# 代码9-4
from test_paper import Test_Paper
# 抽取试卷
total = Test_Paper.learning_coin()  # 调用函数，获取学习币
print('学习币值为：', total)
topics = Test_Paper.rule(total)  # 调用函数，抽取试卷
print('--------- 试卷抽取完毕 ----------')
print('试卷内容为：', topics)