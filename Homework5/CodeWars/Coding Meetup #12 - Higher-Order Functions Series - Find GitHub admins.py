def find_admin(lst, lang):
    res = []
    for elem in lst:
        if elem['language'] == lang and elem['githubAdmin']=='yes':
            res.append(elem)
    return res

#https://www.codewars.com/kata/582dace555a1f4d859000058/python