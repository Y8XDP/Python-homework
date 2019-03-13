mass = [1, 3, 4, 5, 9, 10, 2, -6, -9, 90, 1000, 80, -24]

i = 0;

while i < int(len(mass) - 1):
    m = int(i)
    j = int(i+1)
    while j < int(len(mass)):
        if int(mass[j]) < int(mass[i]):
            m = int(j)
        j+=1
    mass[i], mass[m] = mass[m], mass[i]
    i+=1
print(mass)