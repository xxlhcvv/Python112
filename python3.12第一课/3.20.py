#列表的创建，分成两种方式方括号[]和list函数

list1 = [1, 2.0, 'one', ['cat', 'dog'], True]
print(list1, type(list1))
list2 = list((1, 2.0, 'one', ['cat', 'dog'], True))
print(list2)
list3 = []  #创建空列表
list4 = list("hello word!")  #拆分
print(list4)

#列表的索引，从0开始
print(list1[3])
#列表的切片，[起始索引：终止索引：步长]（终止索引不包含）
list5 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(list5[::])  #都不写，表示访问全部
print(list5[::2])  #步长为正,每隔1个取1个，取索引0,2,4...
print(list5[::-1])  #步长为负数表示从右往左

list5.append(100)  #append在函数末尾增加一个元素
print(list5)
list_add = [110, 120, 130, 140, 150]
list5.extend(list_add)  #extend函数在末尾增加一个列表
print(list5)
#insert函数在指定位置增加一个元素，第一个参数为索引，第二个为元素值
list5.insert(0, 0)  #index指插在哪里，object指插入什么内容
print(list5)

#列表的删除
del list5[-1]  #del语句，根据索引删除元素
print(list5)
x = list5.pop(0)  #pop函数根据索引删除元素，并获取元素值
print(x)  #x表示删除的那个元素
list5.remove(140)  #remove根据元素值删除
print(list5)

#列表的修改
list5[-1] = 150  #使用赋值的方式修改
print(list5)

#列表方式的使用
list6 = list5.copy()  #copy函数列表副本
print(list6)
print(list6.index(40))  #index函数根据值查看索引
list6[0] = 40
print(list6)
print(list6.count(40))  #count函数计算元素值出现次数
list6.sort(reverse=False)  #sort函数对列表排序，升序;  降序为True
print(list6)
list7 = ['spring', 'summer', 'autumn', 'winter']
list7.reverse()  #反转列表
print(list7)
print(len(list6))  #查看列表元素个数

#制作计算日期对应的星期
week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = int(input("请输入月份:"))
day = int(input("请输入几号:"))
#计算今年一共过了多少天
sum_day = sum(month_day[:month - 1]) + day  #例如2月是1月（31天）加日期，因为2月没过完
print("今年一共过了%d天" % sum_day)  #%d取整数占位，%把右边的变量填充到左边的字符串中
print(week[(sum_day % + 2)%7])  #今年1月1日为星期四，所以要加2

turnover1 = [20, 80, 45, 35, 32, 75, 43]
turnover2 = [54, 34, 23, 54, 34]
turnover3 = turnover1 + turnover2
print(turnover3[1])
turnover3[11] = 46
print(turnover3[11])
