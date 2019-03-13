mass = [1, 3, 4, 5, 9, 10, 2, -6, -9, 90, 1000, 80, -24]

fr = -1
to = -1

ii = 0

while fr < 0 or fr > len(mass):
    fr = int(input())
    if fr < 0:
        print("Не меньше 0")
    elif fr > len(mass):
        print("Не больше количества элементов массива")

while to < 0 or fr > len(mass):
    to = int(input())
    if fr < 0:
        print("Не меньше 0")
    elif fr > len(mass):
        print("Не больше количества элементов массива")

for i in range(fr, to):
    print(mass[i])
