f = open('set_ing_words.txt', 'r')
many_words = [i.split() for i in f]
final_many_words = [item for sublist in many_words for item in sublist]


some_dict = {}
for elem in final_many_words:
    if elem in some_dict:
        some_dict[elem] += 1
    else:
        some_dict[elem] = 1


sorted_some_dict = sorted(some_dict.items(), key = lambda x:x[1], reverse = True)
converted_dict = dict(sorted_some_dict)

print(converted_dict)
f.close()