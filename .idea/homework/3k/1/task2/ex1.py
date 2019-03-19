import random

mass = {}

for i in range(15):
    mass[i] = random.randint(0, 100)

max = mass[0]
min = mass[0]

print("Cгенерироанный массив: " + str(mass))

for i in range(len(mass)):
    if max < mass[i]:
        max = mass[i]
    if min > mass[i]:
        min = mass[i]

print("Максимум: " + str(max) + "\nМинимум: " + str(min))
print(str(max) + " - " + str(min) + " = " + str(max - min))
