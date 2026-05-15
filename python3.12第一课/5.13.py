#读写csv文件
#导入csv模块
import csv
#两种方式进行读取，csv.reader数据保存为列表，csv.DictReader字典
with open('./data/carsales.csv','r',encoding='gbk') as f:
    reader = csv.reader(f)
    carsales=[carsales_item for carsales_item in reader]
    print(carsales)
    print(carsales[2])#列表优势：针对获取某一行数据

with open('./data/carsales.csv','r',encoding='gbk') as f:
    reader = csv.DictReader(f)
    #carsales1=[carsales_item for carsales_item in reader]
    #print(carsales1)
    column=[carsales_item['汽车型号'] for carsales_item in reader]
    print(column)#字典优势：针对获取某一列数据

#将数据写入csv文件
#writerow函数将数据逐行写入csv文件
with open('./data/test1.csv','w',newline='') as f:
    writer_csv = csv.writer(f)
    for carsales_item in carsales:#列表元素为一行数据，所以需遍历
        writer_csv.writerow(carsales_item)
#对于字典形式数据，csv.DictWriter类将数据写入CSV文件

with open('./data/carsales.csv', 'r', encoding='gbk') as f:
    reader = csv.DictReader(f)
    carsales1 = [carsales_item for carsales_item in reader]
    print(carsales1)

my_key = []  # 键的集合
for i in carsales1[0].keys():
    my_key.append(i)
with open('./data/test2.csv', 'w', newline = '') as f:
    write_csv = csv.DictWriter(f, my_key)
    write_csv.writeheader()  # 输入标题
    write_csv.writerows(carsales1)  # 输入数据

