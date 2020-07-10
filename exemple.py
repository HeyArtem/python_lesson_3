#import pymorphy2
#morph = pymorphy2.MorphAnalyzer()
import string
# 1) методами строк очистить текст от знаков препинания;
print()
print('1) без знаков препинания: ')
print()

f = open('123.txt','r', encoding='UTF8')
text_str = f.read()
print(type(text_str))




# знаки препинания
# точка (.), вопросительный знак (?), восклицательный знак (!), многоточие (...),
# запятая (,), точка с запятой (;), двоеточие (:), тире (-), скобки (круглые) ( ), кавычки (" ")

no_sign = ''
sign_list = '. ? ! , ; : \' — ( ) " « »'.split()

for i in sign_list:
    text_str = text_str.replace(i, no_sign)

print(text_str)
print()


# 2) сформировать list со словами (split);

print('2) Список:')
print()

text_list = text_str.split()
print(text_list)
print()


# 3) привести все слова к нижнему регистру (map);
# 5) дополнительно к приведению к нижнему регистру выполнить лемматизацию

print('3) Нижний регист: \n5) Лемматизация:')
print()
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
text_lower = list(map(lambda x: x.lower(), text_list))

lem_list = []

for a in text_lower:
    lem_list.append(morph.parse(a)[0].normal_form)
print(lem_list)
print('*-*')


#3) получить из list пункта 3 dict, ключами которого являются слова,
# а значениями их количество появлений в тексте;

print('4) Словарь: ')
print()

#text_dict = {a: text_lower.count(a) for a in text_lower}
text_dict = {a: lem_list.count(a) for a in lem_list}
print('text_dict > ', text_dict)

for keys, values in text_dict.items():
    print(keys, values)

print()


# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set);

print('5 наиболее часто встречающихся слов:')
print()
# 5 наиболее часто встречающихся слов

popular_words = []
for a in text_dict.values():
    popular_words.append(a)
popular_words.sort()
print('*', popular_words)

popular_5words = popular_words[-5:]
for keys, values in text_dict.items():
    if values in popular_5words:
        print(keys, values)

print()

#количество разных слов в тексте
differ_words = set(text_dict)
print('Количество разных слов в тексте: ', len(differ_words))