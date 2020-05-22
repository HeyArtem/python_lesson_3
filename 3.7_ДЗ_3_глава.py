# Домашнее задание после третье главы. Рожков Артем

import string
f = open('123.txt','r', encoding='UTF8')
text=f.read()
#print(type(text), text)

# 1. Методами строк очистить текст от знаков препинания;
#print('1 Методами строк очистить текст от знаков препинания')

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

#print(type(my_str), my_str)


#2.Cформировать list со словами (split)
#print(' 2.Cформировать list со словами (split) ')
my_str_list = my_str.split()
#print(type(my_str_list), my_str_list)



# 3.привести все слова к нижнему регистру (map);
#print(' 3.привести все слова к нижнему регистру (map) ')
new_list = list(map(lambda x: x.lower(), my_str_list))
#print(type(new_list), new_list)


# 3.(опять п.3) Получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
#print(' 3.(опять п.3) Получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте; ')

my_dict = {a:new_list.count(a) for a in new_list} # это не моё реш. почему a,  (i не льзя)? какая логика
#print(my_dict)






# 4. Bывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
#print(' 4. Bывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set)')

pop_words = []
for a in my_dict.values():
    pop_words.append(a)
pop_words.sort()

pop5words = pop_words[-5:]
for keys, values in my_dict.items():
    if values in pop5words:
#        print(keys, values)

total_words = len(set(my_dict))
#print('Всего в тексте разновидностей слов: ', total_words)



# 5. Выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.
#print(' 5. Выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию. ')
import pymorphy2
morph = pymorphy2.MorphAnalyzer()


my_lemma = []
for a in new_list:
    my_lemma.append(morph.parse(a)[0].normal_form)
#print(my_lemma)

