x = int(input("x: "))
x = abs(x)
count = 0

l = list(str(x))
print(" + ".join([i + "**10**" + str(l[::-1].index(i)) for i in l]))


while x > 0:
    x = x // 10
    count += 1
print("Разрядов: ",count)