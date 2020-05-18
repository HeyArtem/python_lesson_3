# Тип данных КОРТЕЖ (tuple)

        # Инициализация
print(' Инициализация ')
temp_tuple = (1, 2, 3)
print(type(temp_tuple), temp_tuple)

# пРеобразование list в tuple
print(' пРеобразование list в tuple ')

temp_list2 = [3, 4, 5]
temp_tuple2 = tuple(temp_list2) # !!! если нужно ИЗМЕНИТЬ КОРТЕЖ, его конвер-ют в list, а потом обратно в tuple
print(temp_tuple2, type(temp_tuple2))






print()
        # Обращения к элемнтам кортежа
print(' Обращения к элемнтам кортежа ')
print(temp_tuple[0])

# Итерация
for i in range(len(temp_tuple)):
    print(temp_tuple[i])

print()
        # Функции с кортежами
print(' Функции с кортежами ')
# КАК В СПИСКАХ  LIST



print()
        # Опреации с кортежами
print(' Опреации с кортежами ')
# КАК В СПИСКАХ  LIST



print()
        # Методы
print(' Методы ')
# КАК В СПИСКАХ  LIST


# Память, хранени, сравнение с list
print(' Память ОБЬЕМ, хранени, сравнение с list ')

temp_list = [1,2,3]
temp_tuple = (1,2,3)
# Сравним занимаемый обьем памяти
print(temp_list)
print(temp_list.__sizeof__())

print(temp_tuple)
print(temp_tuple.__sizeof__())


