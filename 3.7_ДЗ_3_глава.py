# Домашнее задание после третье главы. Рожков Артем

import string
f = open('123.txt','r', encoding='UTF8')
text=f.read()
print(type(text))

# 1. Методами строк очистить текст от знаков препинания;

my_str = text.replace('.', ' ')
my_str = my_str.replace(',', ' ')
my_str = my_str.replace('—', ' ')
my_str = my_str.replace('»', ' ')
my_str = my_str.replace('«', ' ')
my_str = my_str.replace('!', ' ')
my_str = my_str.replace('?', ' ')
my_str = my_str.replace(';', ' ')
my_str = my_str.replace('-', ' ')
my_str = my_str.replace(')', ' ')
my_str = my_str.replace('(', ' ')
my_str = my_str.replace(':', ' ')

print(type(my_str), my_str)


# 2.Cформировать list со словами (split)
my_str_list = my_str.split()
print(type(my_str_list), my_str_list)

# 3.привести все слова к нижнему регистру (map);
new_list = list(map(lambda x: x.lower(), my_str_list))
print(type(new_list), new_list)

# 3.(опять п.3) Получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
from collections import Counter
new_list2 = Counter(new_list)
print(type(new_list2),new_list2)


# 4. Bывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).



#with open('123.txt', 'r') as file:
#   responce = file.read().replace('\n', ").replace('\r',")






#print(type(my_str))









#responce=file.read().replace('\n',").replace('\r',")

#print(type(my_list))
# Методами строк очистить текст от знаков препинания.
#my_str2 = my_str("{" [.] [" "] [":"]"}")
# my_str2 = my_str.replace('.', 'ЗАМЕНИЛ ТОЧКУ')
#my_str.find('заб', [0], [200])

#my_str2 = my_str.replace('.', 'ЗАМЕНИЛ ТОЧКУ')
#print(my_str2)