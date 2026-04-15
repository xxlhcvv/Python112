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
