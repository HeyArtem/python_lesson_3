
# Тип данных Словарь dict
dict_temp = {}
print(type(dict_temp), dict_temp)

dict_temp = {'dict': 1, 'dict2': 2.1, 'dict3': 'name', 'dict4': [1, 2, 3]}
print(type(dict_temp), dict_temp)

print(' * ')

dict_temp = dict.fromkeys(['a', 'b']) # fromkeys создает словарь с КЛЮЧАМИ без ЗНАЧЕНИЙ
print(type(dict_temp), dict_temp)

print(' * * ')

dict_temp = dict.fromkeys(['a', 'b'], [12, '2020']) # наполняем значениями
print(type(dict_temp), dict_temp)

print(' * * * ')

dict_temp = dict(brend = 'Volvo', volume_engine = 1.5) # dict метод наполнения
print(type(dict_temp), dict_temp)

print(' * * * * ')

        # Генератор словаря
dict_temp = {a: a**2 for a in range(10)}
print(dict_temp)


        # Обращене к содержимому словаря
print(' Обращене к содержимому словаря ')
print(dict_temp[8])

print(' выыод всех ключей СЛОВАРЯ ')
print(dict_temp.keys())

print()
# но обычно приводят к листу
print(' но обычно приводят к листу ')
print(list(dict_temp.keys()))

print(' - - ')

# Получение значений
print(' Получение значений ')
print(list(dict_temp.values()))

print()
# также можно рабоать с парами (ключ:знач) = items, он возвращает КОРТЕЖИ
print(' также можно рабоать с парами (ключ:знач) = items ')
print(list(dict_temp.items()))

print()

        # Работа с элементами
print(' Работа с элементами ')
print(type(dict_temp), dict_temp)

dict_temp[0] = 100 # к опред ключу присвоим значение
print(type(dict_temp), dict_temp)

print(' - - - - - -')

# Добавляем новую ПАРУ
print(' Добавляем новую ПАРУ ')
dict_temp['name'] = 'Dima'
print(type(dict_temp), dict_temp)

print(' / / / / / ')

        # Методы

# Удаляем значение по ключу  pop
print(' Удаляем значение по ключу ')
dict_temp.pop('name')
print(type(dict_temp), dict_temp)

# или вывести значение которое удалил
print('вывести значение которое удалил')

temp = dict_temp.pop(0) # почему оно не удалено!?!?!
print(temp)
print(dict_temp)

print(' *-*-*-*-*-*-*')

# Итерирование по словарю
print(' Итерирование по словарю ')


for pair in dict_temp.items():
    print(pair)

# Итерирование по словарю II способ
print(' * Итерирование по словарю II способ *  ')
for key, value in dict_temp.items():
    print(key, value)

print(' + + + + + + + ')

# Итерирование по ключам
print(' Итерирование по ключам ')
for key in dict_temp.keys():
    print(key)

print('&&&&&&&&&&&&&')

# Итерирование по ЗНАЧЕНИЯМ
print(' Итерирование по ЗНАЧЕНИЯМ ')
for value in dict_temp.values():
    print(value)

