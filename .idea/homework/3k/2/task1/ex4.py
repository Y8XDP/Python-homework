mass = [1, 3, 4, 5, 9, 10, 2, -6, -9, 90, 1000, 80, -24]

val = str(input())

#print(mass[mass.index(val)])

for i in mass:
    if val == str(i): print(i)
    else: print("Не найдено")