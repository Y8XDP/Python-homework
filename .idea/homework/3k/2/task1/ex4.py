mass = [1, 3, 4, 5, 9, 10, 2, -6, -9, 90, 1000, 80, -24]

val = str(input())

#print(mass[mass.index(val)])

isExist = False
valIndex = -1;

for i in range(len(mass)):
    if val == str(mass[i]):
        isExist = True
        valIndex = i

if isExist:
    print("Число " + str(val) + " имеет индекс " + str(valIndex))
else:
    print("Число не найдено")

