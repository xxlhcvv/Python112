#读取文件，使用open函数打开文件，read函数读取文件
f=open(r'D:\Python\python3.12第一课\data\xxlhcvv.txt','r',encoding='utf-8')
txt=f.read()
print(txt)
f.close()

#使用with语句读取文件，自动调用close函数，防止出现异常无法关闭文件
with open('./data/xxlhcvv.txt','r',encoding='utf-8') as f:
    print(f.read())

#使用绝对引用，由于路径中\为转义符，需对路径进行处理
#1、使用/代替\
#2、使用\\表示一个正常的符号\
#在绝对路径的引号前加r