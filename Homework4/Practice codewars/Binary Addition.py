def add_binary(a, b):
    res = ""
    plus = a + b
    while plus > 0:
        res += str(plus % 2)
        plus = plus // 2

    return res[::-1]

#https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python