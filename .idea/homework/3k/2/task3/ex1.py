str = str(input())

i = str.find(".")
str = str[::-1]
j = str.find(".")
str = str[::-1]

print(str[i+1:len(str)-(j+1)])