x = 34
print(id(x))
y = x
print(id(y))
print(x, type(x))

# x = input("第一:")
# y = input("第二:")
# print(x + y)  #字符串相加
# print(int(x) + int(y))  #数字相加

x = 3.0
print(x, type(x))

word = "what's happened"  #或者word='what\'s happened'
print(word, type(word))

price = "Apple\'s unit price is 9 yuan."
print(price[-7])  #或者print(price[22])
print(type(price))  #输出price为字符串型
print(int(price[-7]))
