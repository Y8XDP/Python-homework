s = input()

mass = []

t = ""
for i in s:
    if i == ' ':
        mass.append(int(t))
        t = ""
    else:
        t += str(i)

max = mass[0]

print("Из строки " + s + " собран массив: " + str(mass))

for i in range(len(mass)):
    if max < mass[i]:
        max = mass[i]

print("Максимум " + str(max))
