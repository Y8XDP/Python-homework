mass = [1, 3, 4, 5, 9, 10, 2, -6, -9, 90, 1000, 80, -24]

#print(min(mass)) можно в одну строку

min = mass[0]

for i in mass:
    if min > i:
        min = i;

print(min)
