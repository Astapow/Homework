def my_low(low):

    return low.lower()

def my_upp(up):
    return up.upper()

random_str = ["Hello","i","like","Python"]

str_low = list(map(my_low, random_str))

str_up = list(map(my_upp, random_str))

print(str_up,str_low)
