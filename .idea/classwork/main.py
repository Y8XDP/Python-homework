def facu(a):
    for i in range(a - 1):
        a *= i + 1

    return a

print(facu(int(input())))