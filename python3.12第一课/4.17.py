#匿名函数不使用def语句，没有函数名
#使用lambda函数，避免重复使用
example = lambda x: x ** 3
#lambda后为参数。冒号后为返回值
print(example)  #打印lambda函数地址
print(example(2))


# Python高阶内置函数map
# map(func,list)，func函数，list列表
# 从左到右顺序使用函数对列表元素计算
def add(x):  #自定义函数
    x **= 3
    return x


numbers = list(range(10))  #list函数创建列表
print(list(map(add, numbers)))

# 匿名函数：速度快，可读性高
print(list(map(lambda x: x ** 3, numbers)))


# 多种方式实现数据累加
# （1）使用def关键字定义一个累加函数add
def add(x):
    x += 3
    return x

# （2）创建一个空列表
list1 = []

# （3）使用循环结构for i in range(10)
# 对列表进行数据累加后的元素添加（list.append()）
for i in range(10):
    list1.append(add(i))
print(list1)
# （4）使用匿名函数代替累加函数，并将计算结果添加至列表
list2 = []
lam = lambda x:x+3
for i in range(10):
    list2.append(lam(i))
print(list2)

# （5）使用map函数快速实现数据的累加，以及列表元素的添加
print(list(map(lambda x:x+3, list(range(10)))))



import random #导入内置模块
x = random.randint(0,100)
#使用模块random中的randint函数
print(x)

import steak1 #导入自定义模块
steak1.make_steak(0,'salad')
