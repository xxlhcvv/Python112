#自定义函数def
def sum1(a, b):  #sum1为函数名，a和b为参数
    sum2 = a + b  #代码块，函数实现的功能
    return sum2  #return返回值，不具备打印功能


#函数的调用：函数名（参数）
x = sum1(78, 56)  #参数a=78，参数b=56
print(x)


def multi(a, b, c):
    if a == "*":
        sum = b * c
    return sum


print(multi("*", 6, 7))


#任意位置可变参数*和**
#可变参数*表示多个数据存元组
#可变参数**表示多个数据存字典
def exp(x, y, *a, **b):
    print('x:', x)
    print('y:', y)
    print('args:', a)  #打印可变位置参数a（元组形式）
    print('kwargs:', b)  #打印可变关键字参数b（字典形式）


exp(1, 2, 2, 4, 6, 8, a='c', b=1)

'''使用可变参数完成多个数据的求和'''


def multi_sum(*x):
    sum = 0
    for i in x: #求和函数
        sum += i
    return sum


print(multi_sum(1, 2, 3, 4, 5, 6, 7, 8, 9))
