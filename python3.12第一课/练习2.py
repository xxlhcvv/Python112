import os

os.mkdir('学生信息收集')
print(os.path.exists('学生信息收集'))
path = os.getcwd()
print(path)
list = os.listdir('./data')
print(list)
for item in list:
    source = os.path.join('./data', item)
    destination = os.path.join('./学生信息收集', item)
    os.rename(source, destination)

if os.path.exists('./data'):
    os.rmdir('./data')