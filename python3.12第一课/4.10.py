#自定义函数def
def sum1(a, b):  #sum1为函数名，a和b为参数
    sum = a + b  #代码块，函数实现的功能
    return sum  #return返回值，不具备打印功能


#函数的调用：函数名（参数）
x = sum1(78, 56)  #参数a=78，参数b=56
print(x)


# 1 usage
def multi(a, b, c):
    if a == "*":
        sum = b * c
    return sum


print(multi("*", 6, 7))


