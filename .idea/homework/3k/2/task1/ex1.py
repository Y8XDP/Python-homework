mass = [1, 3, 4, 5, 9, 10, 2, -6, -9, 90, 1000, 80, -24]

min = mass[0]
minIndex = 0;
print("Начальный массив: " + str(mass))

for i in range(len(mass)):
    if min > mass[i]:
        min = mass[i];
        minIndex = i

del mass[minIndex]

print("Минимальный элемент в списке с индексом " + str(minIndex) + " имеет значение " + str(min))
print("Конечный массив: " + str(mass))
