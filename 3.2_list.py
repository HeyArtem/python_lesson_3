# Тип данных список  list

        # Инициализация (генераторы)
list_temp = []  # Пустой список
print(type(list_temp))

list_temp = [1.2, 123, 'Volvo', [1, 2, 3]]
for el in list_temp:
    print(el, type(el))

print('*')

list_str = list('Volvo') # Сделает список из элементов
print(list_str)


        # Обращение к элементам списка, подписки
print()
print('Обращение к элементам списка, подписки')
list_temp = [1.2, 123, 'Volvo', [1, 2, 3]]
for i in range(len(list_temp)):
    print(i, ':', list_temp[i])


# Срезы
print()
print('Срезы')

for i in range(len(list_temp)):
    print(i, ':', list_temp[i:])

print(' * ')
for i in range(len(list_temp)):
        print(i, '^', list_temp[:i]) # не пойму!!??!?!?




        # Функции со списками
print()
print(' - Функции со списками - ')
list_temp = [1.2, 123, 'Volvo', [1, 2, 3]]

print(len(list_temp))

        # Операции со списками
print()
print('- Опреации со списками -')
print(list_temp +  list_str) # Конкатенация
print(list_temp * 2)



        # Методы
print()
print('- Методы - ')

# append -добавление к концу

integer_list = []
for i in range(5):
    integer_list.append(i)
print(integer_list)

print(' * ')

# append
for i in range(10):
     list_temp.append(i)
print(list_temp)

print(' * * ')

integer_list.append(100)
print(integer_list)

print(' * * * ')

# remove   удаление из списка

integer_list.remove(100)
print(integer_list)

print(' или ')

integer_list.append(0)
print(integer_list)

integer_list.remove(0) # удаляет первый по вхождению (первого встретившегося)
print(integer_list)

print('Удаление по индексу')
print(integer_list)
del integer_list[4]
print(integer_list)

print('- * - * ')

# revers    изменнение порядка
print(' revers    изменнение порядка ')

print(integer_list)
integer_list.reverse()
print(integer_list)

# sort   сортировка
print()
print(' # sort   сортировка  ')
new_list = [9, 1, 7, 2, 8, 3, 4, 1, 9,]
new_list.sort()
print(new_list)

# insert   вставлять
print()
print(' # insert   вставлять')
new_list.insert(2, 'xyz')   # ( куда вставляем, что вставляем)
print(new_list)


print()
print(' /-/ /-/ /-/ /-/ /-/ /-/ /-/ /-/ /-/ /-/ /-/ /-/ /-/ /-/ /-/ /-/ ')

        # Обработка списков (map, filter)
print(' # Обработка списков (map, filter) ')

# map  поз-ет сразу делать каку-то операц. посл-но над каждым членом
integer_list = [9, 3, 6, 2, 4,]
print(integer_list)
new_integer_list = list(map(str, integer_list))  #!! от map нужно приводить обратно в list ( т.к. map изменяет)
print(new_integer_list)

print(' * ')

new_integer_list2 = list(map(lambda x: x**2, integer_list))    # в степень
print(new_integer_list2)


print()
print('\ | \ | \ | \ | \ | \ | \ | \ | \ | \ | \ | \ | ')
# filter    правда тут еще и лямда
print('filter  filter  filter  ')

print(integer_list)

new_integer_list = list(filter(lambda x: x<5, integer_list)) # отфиль-ли и оставили все х<5
print(new_integer_list)

print()

# reduce
print('  reduce     reduce     reduce     reduce     reduce     reduce     reduce     reduce   ')
# Обращ-ся ко всем элем-ам списка и возвр-ет один эле-т

from functools import reduce

integer_list = [1, 2, 3, 4,]
print(integer_list)
sum = reduce(lambda x,y: x+y, integer_list)
priduct = reduce(lambda x,y: x*y, integer_list)
print(sum, priduct)