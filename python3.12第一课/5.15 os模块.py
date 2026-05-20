import os
print(os.name)
print(os.sep)
path=os.getcwd()
print(path)
print(os.listdir(path))
list=os.listdir(path)
for item in list:
    print(item)