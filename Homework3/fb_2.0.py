f = open('fizbuz.txt', 'r')
fizbuz_result = open('fizbuz_result.txt', 'w')
for line in f:
    new_list = line.split()


    fizz = int(new_list[0])
    buzz = int(new_list[1])
    total = int(new_list[2])


    result = ""

    for i in range(1,total+1):
        if not i % fizz and not i % buzz:
            result += 'FB '
        elif not i % fizz:
            result += 'F '
        elif not i % buzz:
            result += 'B '
        else:
            result = result + str(i) + " "
    result += "\n"
    fizbuz_result.write(result)
f.close()
fizbuz_result.close()

