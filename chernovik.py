
f = open('123.txt','r', encoding='UTF8')
text=f.read()
#print(type(text), text)

my_list =text.split() #конвертация str в list, удалили знаки препинания (очень коряво удалили)
#print(type(my_list),my_list)

my_dict = {}
for word in my_list:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

#print(type(my_dict))
#print(my_dict)


# сортировка словаря по возрастанию значения
from collections import OrderedDict
from operator import itemgetter

sorted_dict = OrderedDict(sorted(my_dict.items(), key = lambda t: t[1]))
#print(sorted_dict)

sorted_dict2 = OrderedDict(sorted(my_dict.items(), key = itemgetter(1)))
#print(sorted_dict2)

# сортировка, 5 самых больших по значениям
# output = []
# output = OrderedDict()
# for k,v in sorted_dict:
#     if k not output:
#         output[k] = v
#         if len(output) == 5:
#             break
# print(output)



# for value in sorted(new_list2.values()): # вывод значение из словаря
#     print(type(value), value)




# ПРобую выводить популярные слова из текста
#вывести на экран 10 самых часто встречаемых слов в тексте, которые больше 1 символа(т.е. исключить союзы "и, а, в, с")
# работает, но нужно с количеством слов
# txt11 = '''She sells sea shells on a a a a a a a a a a a a a a a a a a a a the sea shore;
# The shells that she sells are sea shells Im sure.
# So if she sells,.!?;: sea shells on the sea shore,
# Im sure that the shells are,.!?;: b b b b b b b b b b b b b b b b b b b sea shore shells.'''
# punct = ',.!?;:'
# ltxt = [w.rstrip(punct).lower() for w in txt11.split() if len(w.rstrip(punct)) > 1]
# print(type(ltxt))
# print(ltxt)
# print(sorted(set(ltxt), key=ltxt.count, reverse=True)[:5], sep = '\n')




# выводит популярное слово и количество вхождений
# text123 = 'a a a a the the the the'
# l_text = text123.split()
# s_text = set(text123.split())
#
# MyData = sorted(zip([l_text.count(w) for w in s_text], s_text), reverse=True)
# for txt1 in MyData:
#     if (txt1[0] >= MyData[0][0]):
#         ResData = txt1
# print(ResData)





# метод sort
print(' *  МЕТОД sort * ')
x = ({'и': 36, 'в': 28, 'не': 19, 'он': 18, 'с': 15, 'что': 12, 'на': 10, 'да': 10, 'как': 9, 'то': 9, 'все': 7, 'было': 7, 'его': 7, 'это': 6, 'ах': 6,})
#xax = ['все', 'счастливые', 'семьи', 'похожи', 'друг', 'на', 'друга', 'каждая', 'несчастливая', 'семья', 'несчастлива', 'по', 'своему', 'все', 'смешалось', 'в', 'доме', 'облонских', 'жена', 'узнала', 'что', 'муж', 'был', 'в', 'связи']

#xax = [1, 2, 8, 98, 45, 333, 23, 63, 9632, 454, 89, 456, 123, 0, 4, 8,]

#x.sort(reverse=False)
#print(x)
print(type(x))



# Я хочу научится читать функцию!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def total(initial=5, *numbers, extra_number):
#     count = initial
#     for number in numbers:
#         count += number
#     count += extra_number
#     print(count)
#
# total(10, 1, 2, 3, extra_number=50)
#total(10, 1, 2, 3)
# Вызовет ошибку, поскольку мы не указали значение
# аргумента по умолчанию для 'extra_number'.


# def maximum(x, y):
#     ''''
#     Выводит максимум
#     из двух чисел
#
#     '''
#
#     if x > y:
#         return x
#     elif x == y:
#         return 'Числа равны.'
#     else:
#         return
#
# print(maximum(2, 3))
#
# print(maximum.__doc__)


# Словарь из Кортежей
# colors = {}
# color_counts = [('red', 2), ('green', 1), ('blue', 3), ('purple', 5)]
# for color, n in color_counts:
#     colors[color] = n
# print(colors)
my_list = [a+b for a in 'Artem' if a!='e' for b in 'rozhok' if b !='h']
print(type(my_list), my_list)

my_list.append('d')
print(type(my_list), my_list)


l=[1,2,3,5,]
my_list.extend(l)
print('.extend', my_list)


my_list.insert(1, 'Ao')
print('.insert', my_list)

my_list.remove('Ao')
print('.remove ', my_list)

my_list.pop(0)
print(('.pop '), my_list)


# index возвращает индекс указанного элемента. Если таких элементов несколько, вернет индекс только первого.
# Если таких элементов нет,генерируется исключение. Вторым и третьим аргументом можно указать срез для поиска.
#my_list.index('Az', 0, 5)
print(my_list.index('Az', 0, 5))

# возвр-ет количество вхожд. указ-го эле-та
print(my_list.count('Ao'))


#  sorted()  Чтобы получить кортеж с отсортированными элементами, используйте sorted()
# sorted() работает со всеми итерируемыми объектами:
# a = (1,8,6,9,1,4,3,0)
# sorted(a)
# print(type(a),a)

# сорт-ка по алфавиту
print(sorted({'и': 36, 'в': 28, 'не': 19, 'он': 18, 'с': 15, 'что': 12, 'на': 10, 'да': 10, 'как': 9, 'то': 9, 'все': 7, 'было': 7, 'его': 7,}))

# сор-ка по алфавиту, без ключа сорт-ка в перы очередь по регистру
print(sorted("This is a test string from Andrew".split(), key=str.lower))


# сорт-ка по возрастанию возраста, еслли поменять на [1], то по группе
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
    ]
print(sorted(student_tuples, key=lambda student: student[2]))





# # sorted c классами
# print(' sorted c классами ')
# class Student:
#     def __init__(self, name, grade, age):
#         self.name = name
#         self.grade = grade
#         self.age = age
#
#     def __repr__(self):
#         return repr((self.name, self.grade, self.age))
#
#     def weighted_grade(self):
#         return 'CBA'.index(self.grade) / self.age
# student_objects = [
#         Student('john', 'A', 15),
#         Student('jane', 'B', 12),
#         Student('dave', 'B', 10),
#     ]
# print(sorted(student_objects, key=lambda student: student.age))





# Чтобы создать стандартный порядок сортировки для класса, просто добавьте реализацию соответствующих методов сравнения:
#
# >>> Student.__eq__ = lambda self, other: self.age == other.age
# >>> Student.__ne__ = lambda self, other: self.age != other.age
# >>> Student.__lt__ = lambda self, other: self.age < other.age
# >>> Student.__le__ = lambda self, other: self.age <= other.age
# >>> Student.__gt__ = lambda self, other: self.age > other.age
# >>> Student.__ge__ = lambda self, other: self.age >= other.age
# >>> sorted(student_objects)
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]









#  list.sort(key=None, reverse=False) Сортирует элементы в списке по возрастанию.
#  Для сортировки в обратном порядке используйте флаг reverse=True.
# sort  только для списков
asd = ['as', '1', 'tr', 'gf', 'er']
asd.sort()
print('.sort', asd)

print('/ * / * / * / ')




# from _collections import defaultdict # при подсчете вхождений он возвращает строку
# my_dict2 = defaultdict(int)
# for word in my_list:
#     my_dict2[word] += 1
#
# #print(type(my_dict2))
# #print()
#print(my_dict2)