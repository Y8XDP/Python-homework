import math

x = float(input())
y = float(input())

t = math.sqrt(pow(x,2) + pow(y, 2))

if t <= 1 and t > 0:
    if x < 0 and y < 0:
        print("Не попадает")
    else:
        print("Попадает")
else:
    print("Не попадает")