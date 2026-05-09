with open(r'D:\Python\python3.12第一课\data\content.txt', 'r', encoding='utf-8') as f:
    content_list = f.readlines()
print("文件内容（列表形式）：")
print(content_list)
print("\n格式化后的文件内容：")
for line in content_list:
    print(line.strip())