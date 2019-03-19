a = 10
b = 0.01

print((pow((a+b), 4) - (pow(a, 4) + 4*pow(a, 3)*b)) / (6 * pow(a, 2) * pow(b, 2) + 4 * a * pow(b, 3) + pow(b, 4)))