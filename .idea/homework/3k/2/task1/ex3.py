mass = [1, 3, 4, 5, 9, 10, 2, -6, -9, 90, 1000, 80, -24]
print(mass)

b = True;

for i in mass:
    if b:
        if mass.index(i) < len(mass) - 1:
            t2 = mass.index(i);
            mass[t2], mass[t2 + 1] = mass[t2 + 1], mass[t2]
        b = False
    else:
        b = True

print(mass)
