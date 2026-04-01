mydict1 = {'name': '张三', 'age': 20}
#字典的增加，通过键赋值的方式
mydict1['address'] = '江西省赣州市'
print(mydict1)
mydict2 = {'学院': '信息工程学院', '专业': '人工智能'}
mydict1.update(mydict2)
print(mydict1)

#字典的删除：del语句，pop方法。clear方法
del mydict1["address"]  #根据键进行删除
print(mydict1)
age = mydict1.pop('age')  #根据键删除的同时获取值
print(age)
print(mydict1)
mydict1.clear()  #清空字典，注意不是删除字典，会变成空字典
print(mydict1)

#获取字典中的元素信息：keys，values，items
mydict3 = {'name': '张三', 'age': 20, 'address': '江西省赣州市'}
print(mydict3.keys())
print(mydict3.values())
print(mydict3.items())

fruit1 = {'苹果': 154, '香梨': 69, '香蕉': 38}
fruit2 = {'火龙果': 33, '车厘子': 54}
print(fruit1['苹果'])
fruit1['苹果'] = 50
fruit2.pop('车厘子')
fruit1.update(fruit2)
print(fruit1)
total = sum(fruit1.values())
print(total)
