# Множество set

        # Инициализация
temp_set = {} # если ПУСТЫЕ скобки --> СЛОВАРЬ (dict)
print(type(temp_set), temp_set)

temp_set = {1, 2, 3} # если НЕ ПУСТЫЕ скобки --> МНОЖЕСТВО (set)
print(type(temp_set), temp_set)


print()
# Конвертируем  list (список) --в--> set (множество)
print(' Конвертируем  list (список) --в--> set (множество) ')
temp_list = [1, 2, 2, 1, 30, 21, 4, 4, 70, 6]
temp_set = set(temp_list)
print(type(temp_set), temp_set) # мы увидим УНИКАЛЬНОСТЬ элементов


print()
        # Обращение к элементам множества
print(' Обращение к элементам множества ')
# Проверим наличие опред. элем-та в множестве
print(1 in temp_set)
print(100 in temp_set)


print()
# Итерация set множества (! НЕТ ИНДЕКСОВ!)
print(' Итерация set множества (! НЕТ ИНДЕКСОВ!) ')
for element in temp_set:
    print(element)

print()
        # Фунции с множествами- Стандартные
print(' # Фунции с множествами- Стандартные ')




print()
        # Операции с множествами (обьединение, перечеч, разн, симетричРазность
print(' # Операции с множествами (обьединение, перечеч, разн, симетричРазность ')

# Объединение
print(' Создадим Объединение ')
my_set1 = set([1, 2, 3, 4, 5])
my_set2 = set([5, 6, 7, 8, 9])

my_set3 = my_set1.union(my_set2)
print(my_set3)

print(' * * ')
# Разность my_set1 без my_set2
print(' Разность my_set1 без my_set2 ')

my_set4 = my_set1.difference(my_set2)
print(my_set4)