x = int(input())
i = 1
while i <= x:
    if not x % i:
        print(i, end=' ')
    i+=1