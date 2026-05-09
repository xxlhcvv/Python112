#算数运算符
print(10 / 3)
print(10 // 3)  #取整数
print(10 % 3)  #取余数
print(10 ** 3)  #10的3次方

#比较运算符
print(3 == 5)
print(3 != 5)  #3不等于5
print(3 > 5)
print(3 < 5)

#赋值运算符
a = 10
a += 5  #a=a+5，加赋值
print(a)
a -= 5  #a=a-5,减赋值
print(a)
a *= 5  #a=a*5，乘赋值
print(a)
a /= 2  #a=a/5,初复制
print(a)

#按位运算符
print(bin(5))  #求5的二进制
print(5 & 1)  #ob101&ob001,为方便对比写成001(相同为1，不同为0，结果取十进制）
print(int('1', 2))  #计算1的十进制
print(5 ^ 3)  #ob101^ob110,（相同为0，不同为1，结果取十进制）
print(int('110', 2))  #110的十进制为6
print(5 << 1)  #左移<<等价于*2
print(12 >> 2)  #右移>>等价于/4

#逻辑运算符
#and：两边都为真，结果才为真
print(3 > 1 and 5 > 2)   # True and True → True
print(3 > 5 and 5 > 2)   # False and True → False
#or：只要有一个真，结果就为真
print(3 > 5 or 5 > 2)    # False or True → True
print(3 > 5 or 2 > 5)    # False or False → False
#not：真变假，假变真
print(not 3 > 5)         # not False → True
print(not 5 > 2)  # not True → False

x=3+5%6*2/10
print(3+5%6*2/10)
