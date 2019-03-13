mass = [1, 3, 4, 5, 9, 10, 2, -6, -9, 90, 1000, 80, -24]

i = 0;

for i in range(len(mass)):
    for j in range(len(mass)):
        if mass[i] < mass[j]: mass[i], mass[j] = mass[j], mass[i]

print(mass)