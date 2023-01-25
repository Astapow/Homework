a = int(input("fizz: "))
b = int(input("buzz: "))
c = int(input("total: "))

for i in range(1,c+1):
    if not i % a and not i % b:
        print("FB")
    elif not i % a:
        print("F")
    elif not i % b:
        print("B")
    else:
        print(i)
