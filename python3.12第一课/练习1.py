import csv
height_list = []
weight_list = []
with open('./data/height_weight.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        height = float(row['身高/cm'])
        weight = float(row['体重/kg'])
        height_list.append(height)
        weight_list.append(weight)
def mean(data):
    return sum(data) / len(data)

def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)

height_mean = round(mean(height_list), 2)
height_var = round(variance(height_list), 2)
weight_mean = round(mean(weight_list), 2)
weight_var = round(variance(weight_list), 2)
result_data = [
    {'字段': '身高/cm', '均值': height_mean, '方差': height_var},
    {'字段': '体重/kg', '均值': weight_mean, '方差': weight_var}
]
with open('./data/result_mean_var.csv', 'w', newline='', encoding='gbk') as f:
    writer = csv.DictWriter(f, fieldnames=['字段', '均值', '方差'])
    writer.writeheader()
    writer.writerows(result_data)

print("身高均值:", height_mean)
print("身高方差:", height_var)
print("体重均值:", weight_mean)
print("体重方差:", weight_var)