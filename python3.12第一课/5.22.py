import re
text1 = '正则表达式一般由一些普通字符和一些元字符组成。'+\
        '正则表达式是一种可以用于模式匹配和替换的工具'
print(re.findall('正则表达式', text1))
print(re.findall('一[般些]', text1)) #匹配「方括号内的任意一个字符」


import re
str = input("请输入你的电话号码：")
if len(re.findall('^1[39]\\d{9}$', str)):
    print("格式正确！")
else:
    print("请输入正确的电话号码！")