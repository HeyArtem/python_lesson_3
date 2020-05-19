
f = open('123.txt','r', encoding='UTF8')
text=f.read()
#print(type(text), text)

my_list =text.split() #конвертация str в list, удалили знаки препинания
print(type(my_list),my_list)

my_dict = {}
for word in my_list:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

print(type(my_dict))
print(my_dict)


# сортировка словаря по возрастанию значения
from collections import OrderedDict
from operator import itemgetter

sorted_dict = OrderedDict(sorted(my_dict.items(), key = lambda t: t[1]))
print(sorted_dict)

sorted_dict2 = OrderedDict(sorted(my_dict.items(), key = itemgetter(1)))
print(sorted_dict2)




















# from _collections import defaultdict # при подсчете вхождений он возвращает строку
# my_dict2 = defaultdict(int)
# for word in my_list:
#     my_dict2[word] += 1
#
# #print(type(my_dict2))
# #print()
#print(my_dict2)