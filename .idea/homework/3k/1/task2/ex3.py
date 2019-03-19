k = float(input())

s = True

if k % 1 == 0 and k > 1:
    i = 2

    while s and i < k:
        if k % i == 0:
            s = False
        i += 1
else:
    s = False

if s:
    print("Простое")
else:
    print("Не простое")