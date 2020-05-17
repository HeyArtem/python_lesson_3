# Тип данных строка  (str)

        # Инициализация
temp_str = 'Марка авто "Volvo"'
print(temp_str)
# Экранирование
#temp_str = 'Марка авто \'Volvo\'

        # Обращение к символам, подстрокам

# выведет в кажд-ю строку, одну букву. Вывод ПОСИМВОЛЬНО
for i in range(len(temp_str)):
    print(temp_str[i])

# Срезы
print(temp_str[1:4])
print(temp_str[:])
print(temp_str[0:]) # одинарный срез
print('--')
print(temp_str[-3:3]) # это не печатает!?!?!
print('*')
print(temp_str[1:-3])
print('- Конец срезы -')

        # Функ-ции со строками
print(temp_str, len(temp_str))
print('- Конец Функ-ции со строками -')

        # Операции со строками
print()
print('- Операции со строками -')

temp_str2 = 'Mersedes'
print(temp_str + temp_str2)  # !!!!! рекомен НЕ ПОЛЬЗОВАТЬСЯ + , т.к. трудоемко компику!!!
print(temp_str2 * 2)
print('- Конец Операции со строками -')


        # Форматирование строк
# Строки это не изменяемый тип, поэтому проще создать новую
print()
print('- Форматирование строк -')
car = 'Марка: {} цена: {}'.format('Volvo', 1.5)
print(car)

print(' *')

brend = 'Volvo'
price = 1.5
car2 = 'Марка: {} цена: {}'.format(brend, price)
print(car2)

print('* *')

car3 = f'Марка: {brend} цена: {price}'  # это самый ПРЕДПОЧТИТЕЛЬНЫЙ способ
print(car3)

print('- Конец Форматирование строк -')

        # Методы
print()
print('- Методы -')
print(temp_str.split())

print('*')
cars = 'Volga,Audi,BMW,Reno,Lada,SAAB'
print(cars.split()) # Разобьет на отде-е элементы (если есть пробелы!!!)
print(cars.split(',')) # мы указали РАЗДЕЛИТЕЛЬ!!! и...

print('* *')

# Методы форматирования строк
print(cars.upper()) # все буквы ЗАГЛАВНЫЕ
print('* * *')

print(cars.title())  # ПЕРВЫЕ буквы ЗАГЛАВНЫЕ
print(cars.lower())  # все буквы маленькие
print('* * * *')

# Замена подстроки в строке
my_kontakt = 'eMail: _xxx_'
eMail2 = 'artem_white@mail.ru'
print(my_kontakt.replace('_xxx_', eMail2))


print('- Конец  Методы -')