def order_food(lst):
    count = {}
    for i in lst:
        if i['meal'] in count:
            count[i['meal']] += 1
        else:
            count[i['meal']] = 1
    return count

#https://www.codewars.com/kata/583952fbc23341c7180002fd/train/python