import math

x = float(input())
y = float(input())

t = math.sqrt(pow(x,2) + pow(y, 2))

if t <= 1:
    print("Попадает")
else:
    print("Не попадает")