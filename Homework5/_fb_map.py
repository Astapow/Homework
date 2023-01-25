fizbuz_result = open('fizbuz_result.txt', 'w')

fizz = list(map(int, range(1,21)))
buzz = list(map(int, range(10,30)))
total = list(map(int, range(20,40)))

print(f'fizz: {fizz} \n'
      f'buzz: {buzz} \n'
f'total: {total} \n'
)


result = ""

for i in range(0,20):
    f = fizz[i]
    b = buzz[i]
    t = total[i]
    for elem in range(1,t+1):
        if not elem % f and not elem % b:
            result += 'FB '
        elif not elem % f:
            result += 'F '
        elif not elem % b:
            result += 'B '
        else:
            result = result + str(elem) + " "

    result += "\n"
print(result)
fizbuz_result.write(result)
fizbuz_result.close()
