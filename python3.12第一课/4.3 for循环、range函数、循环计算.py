#循环结构语句for
for a in [1, 2, 3]:  #遍历列表
    print(a)

for a in 'hello world':  #遍历字符串
    print(a)

#range函数，range（起始值，终止值，步长）终止值不包含
for i in range(0, 9, 2):
    print(i)  #打印0 2 4 6 8

#计算0~100的整数和
sum=0
for i in range(0,101):
    sum+=i
print("0~100的整数和为:",sum)

# 计算0~100的偶数和、奇数和
sum_b = 0
for i in range(0,101,2):  # 奇数改为range(1,101,2)
    sum_b = sum_b + i
print("0-100的偶数整数和为: ",sum_b)

# 循环结构中使用条件分支
sum_x = 0  # 偶数和
sum_y = 0  # 奇数和
for i in range(0,101):
    if i % 2 == 0:  # 偶数
        sum_x += i
    else:  # 奇数
        sum_y += i
print("偶数和为: ",sum_x)
print("奇数和为: ",sum_y)

# 嵌套循环
for i in range(1,10):  # 0,1,2,3
    for j in range(1,i+1):  # 0,1,2,3
        print(i,"*",j,"=",i*j,"  ", end='')  # 4*4个星号
    print()