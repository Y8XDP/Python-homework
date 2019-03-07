n = float(input())
m = float(input())

m += 1

if m > n:
    print(str(m) + ">" + str(n))
elif m == n:
    print(str(m) + "=" + str(n))
else:
    print(str(m) + "<" + str(n))

n -= 1