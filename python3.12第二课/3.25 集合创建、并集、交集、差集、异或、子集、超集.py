#花括号创建，元素不可重复，自动去重
myset1 = {"a", "b", "c", "a", "b"}
print(myset1)

#set()函数创建：可转换列表/元组等，空集合必须用set()
myset2 = ([2, 3, 1, 4, False, 2.5, "one"])  #False在哈希值中相当于0，顺序为整形浮点型字符串
print(myset2)

#空可变集合
empty_set = set()
print(type, empty_set)

myset3 = frozenset([3, 2, 3, "one", frozenset([1, 2]), True])  #不可变集合
print(myset3)
print(type, myset3)
#空不可变集合
empty_frozenset = frozenset()
print(type, empty_frozenset)

scores = ("语文:78", "数学:89", "外语:89", "政治：90", "实践：69")
print(scores[4])

A = {'足球', '游泳', '羽毛球', '乒乓球'}
B = {'篮球', '乒乓球', '羽毛球', '排球'}

# 1. 并集（A/B所有元素，去重）| / union()
print(A | B)
print(A.union(B))  # 结果均为{'羽毛球', '排球', '乒乓球', '足球', '篮球', '游泳'}

# 2. 交集（A/B共有元素）& / intersection()
print(A & B)
print(A.intersection(B))  # 结果均为{'羽毛球', '乒乓球'}

# 3. 差集（A有B无）- / difference()
print(A - B)
print(A.difference(B))  # 结果均为{'游泳', '足球'}

# 4. 异或集（A/B独有元素，无共有）^ / symmetric_difference()
print(A ^ B)
print(A.symmetric_difference(B))  # 结果均为{'游泳', '篮球', '足球', '排球'}

A = {'足球', '游泳', '羽毛球', '乒乓球'}
C = {'足球', '乒乓球', '游泳'}
# 子集（C所有元素在A中）<= / issubset()
print(C <= A)
print(C.issubset(A))  # 均为True

# 真子集（C是子集且A包含C没有的元素）<
print(C < A)  # True
print(A < A)  # False

# 超集（A包含C所有元素）>= / issuperset()
print(A >= C)
print(A.issuperset(C))  # 均为True

# 真超集（A是超集且包含C没有的元素）>
print(A > C)  # True
print(C > C)  # False

myset4 = {'red', 'green', 'blue', 'yellow'}
myset4_copy = myset4.copy()  # 复制集合
others = {'black', 'white'}  #others其他集合

# 增：add(单个元素)、update(合并其他集合)
myset4.add('orange')
myset4.update(others)  #把others合并到myset4中
print(myset4)  # {'black', 'green', 'yellow', 'orange', 'white', 'blue', 'red'}

# 删：pop(随机删1个)、remove(指定删1个)、clear(清空所有)
print(myset4.pop())  # 随机输出如'black'
print(myset4)
myset4.remove('yellow')
print(myset4)
myset4_copy.clear()
print(myset4_copy)  # 输出空集合set()

# 查：len(获取元素个数)
print(len(myset4))  # 5
