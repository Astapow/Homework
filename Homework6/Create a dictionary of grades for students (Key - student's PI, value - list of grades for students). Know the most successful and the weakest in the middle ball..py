students = dict([
    ('ivanov',[2,4,6]),
    ('petrov',[1,3,6]),
    ('sidorov',[4,6,2]),
    ('efimov',[8,3,5])
])


def get_avg(lst):
    return sum(lst)/len(lst)


def top_students(studs):
    max_elem = 0
    max_key = ''
    for key,val in studs.items():
        avg = get_avg(val)
        if avg > max_elem:
            max_elem = avg
            max_key = key
    return max_key, round(max_elem, 2)


def low_students(studs):
    low_elem = 100
    low_key = ''
    for key, val in studs.items():
        avg = get_avg(val)
        if avg < low_elem:
            low_elem = avg
            low_key = key
    return low_key, round(low_elem, 2)

print (top_students(students))
print (low_students(students))