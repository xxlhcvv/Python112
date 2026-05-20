import math
num = float(input("请输入一个数值："))
cos_result = math.cos(num)
asin_result = math.asin(num)
log_result = math.log(num)
sqrt_result = math.sqrt(num)

print(f"cos({num}) = {cos_result}")
print(f"asin({num}) = {asin_result}")
print(f"log({num}) = {log_result}")
print(f"sqrt({num}) = {sqrt_result}")