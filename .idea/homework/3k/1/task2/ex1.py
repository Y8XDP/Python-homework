import random

mass = {}

for i in range(15):
    mass[i] = random.randint(0, 100)

max = mass[0]
min = mass[0]

for i in range(len(mass)):
    if max < mass[i]:
        max = mass[i]
    if min > mass[i]:
        min = mass[i]

print(max - min)
