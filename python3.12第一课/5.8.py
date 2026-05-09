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
#3、在绝对路径的引号前加r

#按行读取文件，寻找特定信息，使用for循环遍历
with open('./data/xxlhcvv.txt','r',encoding='utf-8') as f:
    for line_t in f:
        print(line_t.rstrip()) #rstrip函数删除末尾换行符\n

#使用readlines函数将文本存进列表中，每一行为一个元素
with open('./data/xxlhcvv.txt','r',encoding='utf-8') as f:
    txts= f.readlines()
    print(type(txts))
    print(txts[2]) #查看文本第3行的内容

#写入文件，标识符设置为“w”，若文件不存在，则创建文件
with open('./data/zzx.txt','w',encoding='utf-8') as f:
    f.writelines('hello world')
    #使用write函数