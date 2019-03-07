n = float(input())
m = float(input())

m = m/n

if m > n:
    print(str(m) + ">" + str(n))
elif m == n:
    print(str(m) + "=" + str(n))
else:
    print(str(m) + "<" + str(n))

n -= 1