#嵌套函数：函数内部定义函数，叫做内置函数
#全局变量和局部变量
#局部变量作用于函数内部
#全局变量在函数外定义，可以在函数内部使用，但不能被赋值
def mean(*args):
    m=0
    def sum(x):
        sum1=0 #sum1为局部变量，sum函数外部不能使用
        for i in x: #遍历元组
            sum1 += i
        return sum1
    m=sum(args)/len(args)
    return m
print(mean(1,89,67,45,234))

#构建计算用餐总价格的函数
def day_income(unit_price,*table_count):
    sum_price = 0
    def sum(x):
        sum1 = 0
        for i in x:
            sum1 += i
        return sum1
    sum_price = sum(table_count) * unit_price
    return sum_price

print(day_income(10, 12,9,7,10,7,6,11,9,8,11))

#构建求方差函数
def var(*args):
    def sum(x): #求和函数
        sum1 = 0
        for i in x:
            sum1 = sum1 + i
        return sum1

    def mean(z): #算平均数
        m = 0
        m = sum(z) / len(z)
        return m

    def sums(y): #离均差平方和：每个数减去平均值，再平方，然后把所有平方加起来
        sums1 = 0
        for i in y:
            sums1 += (i - mean(y)) ** 2
        return sums1

    return sums(args) / len(args)


print(var(45, 78, 90, 78, 56))
