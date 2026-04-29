#生成迭代器
class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.info=[self.name,self.age]
        self.index=-1
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def __iter__(self):#迭代函数
        print('名字,年龄')
        return self
    def next(self):
        if self.index==len(self.info)-1:
            raise StopIteration
        self.index+=1
        return self.info[self.index]
newcat=cat('coffe',3)
print(newcat.getName())
#调用迭代函数
iterator=iter(newcat.next,1)
for info in iterator:
    print(info)