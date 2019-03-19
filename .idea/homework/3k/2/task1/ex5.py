mass = [1, 3, 4, 5, 9, 10, 2, -6, -9, 90, 1000, 80, -24]

i = 0
print("Начальный массив: " + str(mass))

while i < len(mass) - 1:
    m = i
    j = i + 1

    while j < len(mass):
        if mass[j] < mass[m]:
            m = j
        j += 1
    mass[i], mass[m] = mass[m], mass[i]
    i += 1

print("Сортированный массив: " + str(mass))