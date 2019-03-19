import random

mass = [1, 3, 4, 5, 9, 10, 2, -6, -9, 90, 1000, 80, -24]

fr = -1

print("Начальный массив: " + str(mass))

while fr < 0 or fr > len(mass):
    fr = int(input())
    if fr < 0:
        print("Не меньше 0")
    elif fr > len(mass):
        print("Не больше количества элементов массива")

for i in range(int(input())):
    mass.insert(i+fr, random.randint(500, 600))

print(mass)
