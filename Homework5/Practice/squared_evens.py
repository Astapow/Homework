def my_squad(sq):
    return sq**2

def is_simlpe(check):
    lst = []
    for i in range(2,int(check**0.5) + 1):
        for j in lst:
            if not i % j:
                break
        else:
            lst.append(i)
    return lst

simple_list = list(filter(is_simlpe, range(51)))
print(list(map(my_squad, simple_list)))
