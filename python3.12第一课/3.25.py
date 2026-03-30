#元组和列表的区别：元组不可变（增删改）
#元组的创建：圆括号和tuple函数
mytuple1 = (1, 2.5, ('one', 'two'), ['cat'])
print(mytuple1, type(mytuple1))
mytuple2 = (9,)  #只有一个元素，要有逗号才是元组
print(type(mytuple2))
mylisy = ['name', 'age', 20]
mytuple3 = tuple(mylisy)  #使用tuple函数将其他数据结构改成元组
print(mytuple3, type(mytuple3))

#索引和切片，元组和列表的方法相同
#元组的解包
print(len(mytuple1))
A, B, C, D = mytuple1
print(A, B, C, D)

#元组的重复合并
mytuple4 = mytuple1 * 2
print(mytuple4)

#字典属于键值对映射关系，key->value
#字典的创建：使用{}和dict函数
mydict1 = {'name': '张三', 'age': 20, 'name': '李四'}
#出现相同的键，值取后面那个
print(mydict1, type(mydict1))
#提取字典元素value=dict[key]
print('学生姓名为：%s，年龄为:%s' % (mydict1['name'], mydict1['age']))  #%s是字符串格式化占位符
#如果使用不存在的键查询，会出现报错
#可使用in或者get查看
print('address' in mydict1)
print(mydict1.get('address', '不存在学生地址信息'))  #可设置不存在时打印的内容

