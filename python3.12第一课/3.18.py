#已知圆的半径求周长和面积
r = float(input("r: "))
pai = 3.14
print("圆的周长", pai * r * 2)
print("圆的面积", pai * r ** 2)

#已知圆的面积求半径和周长
s = float(input("s: "))
R = (s / pai) ** (1 / 2)  #求幂运算优先级高于*/.所以要加括号
print("圆的半径", (s / pai) ** 1 / 2)
print("圆的周长", pai * R * 2)

#已知圆的周长求半径和面积
c = float(input("c: "))
a = c / pai / 2
print("圆的半径", a)
print("圆的面积", pai * a ** 2)



