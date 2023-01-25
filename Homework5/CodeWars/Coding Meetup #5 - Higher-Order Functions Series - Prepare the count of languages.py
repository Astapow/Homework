def count_languages(lst):
    lang = {}
    for i in lst:
        if i['language'] in lang:
            lang[i['language']] += 1
        else:
            lang[i['language']] = 1
    return lang


#https://www.codewars.com/kata/5828713ed04efde70e000346/train/python