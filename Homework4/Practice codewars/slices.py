def sum_two_smallest_numbers(numbers):
    TwoSmallest = []
    for i in numbers:
        TwoSmallest.append(i)
    return (sum(sorted(TwoSmallest)[:2]))

#https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python