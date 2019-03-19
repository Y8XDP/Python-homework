s = input()

mass = []

t = ""
for i in s:
    if i == ' ':
        mass.append(int(t))
        t = ""
    else:
        t += str(i)

print(mass)

max = mass[0]

for i in range(len(mass)):
    if max < mass[i]:
        max = mass[i]

print(max)