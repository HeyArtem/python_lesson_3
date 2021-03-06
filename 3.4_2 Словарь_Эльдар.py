''''
Повторяю словари материал от Эльдара

https://github.com/eleldar/base_python_django/blob/master/04_%D0%A1%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D0%B8.ipynb
'''


'''' Простой словарь'''
alien_0 = {'color': 'green', 'points': 5}
print('Простой словарь:', alien_0['color'])
print(alien_0['points'])


''''
Работа со словарями

Словарь в языке Python представляет собой совокупность 
пар «ключ-значение». Каждый ключ связывается с некоторым значением, 
и программа может получить значение, связанное с заданным ключом. 
Значением может быть число, строка, список и даже другой словарь.

СИНТАКСИС
В Python словарь заключается в фигурные скобки {}, в которых приводится последовательность пар «ключ-значение»

Пара «ключ-значение» представляет данные, связанные друг с другом. 
Если вы укажете ключ, то Python вернет значение, связанное с этим ключом. 
Ключ отделяется от значения двоеточием, а отдельные пары разделяются запятыми. 
В словаре может храниться любое количество пар «ключ-значение».
'''

# Простейший словарь содержит ровно одну пару «ключ-значение»
alien_0 = {'color': 'green'} # color - ключ, green - значение
print('По ключу, вызываю значение:', alien_0['color'])


''''
Обращение к значениям в словаре
Чтобы получить значение, связанное с ключом, 
указывается имя словаря, а затем ключ в квадратных скобках
'''

alien_0 = {'color': 'green'}
print(alien_0['color'])


alien_0 = {'color': 'green'}
# print(alien_0['green']) # KeyError: 'green'


# При наличии нескольких пар
alien_0 = {'color': 'green', 'points': 5}
print('Так же вызываю значение по ключу->', alien_0['points'])

''''
Добавление новых пар «ключ-значение»

Словари относятся к динамическим структурам данных: в словарь можно в любой момент добавлять новые пары «ключ-значение».
Для этого указывается имя словаря, за которым в квадратных скобках следует новый ключ с новым значением.

ПРИМЕЧАНИЕ Когда вы выводите словарь или перебираете его элементы, 
вы будете получать элементы в том порядке, в каком они добавлялись в словарь
'''

# Добавим в словарь alien_0 еще два атрибута: координаты x и y
alien_0 = {'color': 'green', 'points': 5}
print('I вар. словаря: ', alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print('II вар. с добавленным X, Y:', alien_0)

alien_0['Далеко'] = 'На лугу пасутся' # Я закрепляю
print(alien_0)


''''
Создание пустого словаря
В некоторых ситуациях бывает удобно (или даже необходимо) 
начать с пустого словаря, а затем добавлять в него новые элементы. 
Чтобы начать заполнение пустого словаря, определите словарь с пустой 
парой фигурных скобок, а затем добавляйте новые пары «ключ-значение» 
(каждая пара в отдельной строке)
'''

alien_0 = {}
print(' Пустой словарь: \n',  alien_0)
alien_0['color'] = 'green'
alien_0['points'] = 5
print(' НЕ Пустой словарь: \n', alien_0)

''''
Изменение значений в словаре

Чтобы изменить значение в словаре, укажите имя словаря с ключом в квадратных скобках, 
а затем новое значение, которое должно быть связано с этим ключом
'''
# Пример изменения значения
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")


# Пример определения величины горизонтального смещения объекта
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position->: {alien_0['x_position']}")


# Объект перемещается вправо.
# Вычисляем величину смещения на основании текущей скорости.
print(alien_0) #{'x_position': 0, 'y_position': 25, 'speed': 'medium'}
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium': # выполняется это условие
    x_increment = 2
else:
    # Объект двигается быстро.
    x_increment = 3

# Новая позиция равна сумме старой позиции и приращения.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"Новая приращённая позиция: {alien_0['x_position']}")


# Вариация
# Изменение одного значения в словаре изменяет все поведение
print('Имеем словарь:\n', alien_0) #{'x_position': 2, 'y_position': 25, 'speed': 'medium'}
alien_0['speed'] = 'fast' #Максимальная скорость
print('Изменили скорость', alien_0) #{'x_position': 2, 'y_position': 25, 'speed': 'fast'}

print(f"Original position: {alien_0['x_position']}") #Original position: 2

# Объект перемещается вправо.
print('    Объект перемещается вправо.')

# Вычисляем величину смещения на основании текущей скорости.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium': # выполняется это условие
    x_increment = 2
else:
    # Объект двигается быстро.
    x_increment = 3
# Новая позиция равна сумме старой позиции и приращения.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")



#Удаление пар «ключ-значение»
print('    Удаление пар «ключ-значение»')
# Удаляется ключ и связанное с ним значение

alien_0 = {'color': 'green', 'points': 5}
print('alien_0-начало:', alien_0)

del alien_0['points']
print('alien_0 после удаления:', alien_0)


''''
Словарь с однотипными объектами

Словарь также может использоваться для хранения одного 
вида информации о многих объектах. 
Допустим, вы хотите провести опрос.
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c++',
    'edward': 'ruby',
    'phil': 'python',
    }

# Для заданного имени участника опроса этот словарь позволяет
# легко определить его любимый язык
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Этот синтаксис может использоваться с любым участником опроса,
# содержащимся в словаре.

# Простейший словарь содержит ровно одну пару «ключ-значение»
alien_0 = {'color': 'green'} # color - ключ, green - значение
# print(alien_0['point']) #KeyError: 'point'


'''' Обращение к значениям методом get() '''
print('    Обращение к значениям методом get() ')

alien_0 = {'color': 'green', 'speed': 'fast'} # color - ключ, green - значение
point_value = alien_0.get('color', 'Sorry!') #зачем здессорри
print('point_value:', point_value)

alien_0 = {'color': 'green', 'speed': 'fast'} # color - ключ, green - значение
print(alien_0.get('color'))







''''
Перебор словаря

Информация может храниться в словарях по-разному, поэтому предусмотрены разные способы перебора. 
Программа может перебрать все пары «ключ-значение» в словаре, только ключи или только значения.
'''

# Перебор всех пар «ключ-значение»
print('    Перебор всех пар «ключ-значение»')



# Пусть имеется словарь.
# В словаре хранится имя пользователя, его имя и фамилия.
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
print('Юзер_0:', user_0)

# Чтобы просмотреть все данные из словаря
# можно воспользоваться перебором в цикле for
# Метод items() возвращает список пар «ключ-значение»
for key,value in user_0.items():
    print(f"\nключ: {key}")
    print(f"Значение: {value}")


# Аналогичный результат
for i, j in user_0.items(): # i, j - переменные
    #print(f"\nKey: {i}")
    print(f"Value: {j}")

# ПРимер словаря Имя:любимый язык
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
# перебор всех пар «ключ-значение» в словаре
for name, language in favorite_languages.items():
    print(f"{name.title()}'s любит язык {language.title()}.")





'''' Перебор всех ключей в словаре'''
print('    Перебор всех ключей в словаре')

''''
Для вывода ключа словаря может использоваться метод key() 
либо вообще ничего не использоваться.
'''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

'''' 
вывода ключа словаря I вар

использование метода key()
из словаря извлекаются все ключи и последовательно сохраняются в переменной name.

!!! # из словаря извлекаются все ключи и последовательно сохраняются в переменной name.
'''
for name in favorite_languages.keys(): # использование метода key()
    print('Выводим все ключи метода key():',name.title())

''''
вывода ключа словаря II вар

Аналогичный результат.
Перебор ключей используется по умолчанию при переборе словаря
'''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
# из словаря извлекаются все ключи и последовательно сохраняются в переменной name.
for name in favorite_languages: # не использую методы
    print('Вывел Ключи без метода', name.title())


print('    Обращение к определенному значению Ключа')
''''
Обращение к определенному значению Ключа

Из словаря извлекаются все ключи и последовательно сохраняются в переменной name.

Переберем имена в словаре и когда имя совпадет с именем одного из друзей, 
выведем специальное сообщение об их любимом языке
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah'] # список друзей, для которых должно выводиться сообщение

for name in favorite_languages.keys(): # цикл проверки имени очередного участника опроса
    print(f"HelloПРивет {name.title()}.")

    if name in friends:   # отдельное сообщение для друзей
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")



# Переберем имена в словаре на предмет отсутствия в списке уастников опроса
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friend = 'stive' # искомое имя
if friend not in favorite_languages.keys(): # проверяет, входит ли ключ  в список
    print(f"{friend.title()}, please take our poll!")




'''' Перебор ключей словаря в определенном порядке '''
print('    Перебор ключей словаря в определенном порядке')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

''''
Простой перебор I вар
'''
print('перебор I вар')
for name in favorite_languages.keys(): # Простой перебор
    print(f"{name.title()}, thank you for taking the poll.")



''''
Перебор II вар

Реализация перебора элементов словаря в другом порядке.
Применение функции 
sorted() 
с использованием цикла for
'''
print('перебор II вар')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()): # Ранжирование
    print(f"{name.title()}, thank you for taking the poll.")
# Примечание: конструкция выдает список всех ключей в словаре и сортирует его перед тем, как перебирать элементы





''''    Перебор всех значений в словаре'''
print('    Перебор всех значений в словаре')

''''
Для получения списка значений без ключей используйтся метод 
values().

Получим список всех языков, выбранных в опросе, 
Имена людей не интересуют
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Были упомянуты следующие языки (мет.values):")
for language in favorite_languages.values():
    print(language.title())

''''
Значения извлекаются из словаря без проверки на возможные повторения. 
Чтобы избавиться от дубликато и получить список выбранных языков без повторений, 
можно воспользоваться множеством 
(set). 

Множество похоже на список, но все его элементы должны быть уникальными.
Получим уникальный список всех языков с использованием ф-ии set()
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'Artem': 'python',
    }
print("Были упомянуты следующие языки (использ.values+set):")
for language in set(favorite_languages.values()):
    print(language.title())


''''
ПРИМЕЧАНИЕ 
Множество можно построить прямо в фигурных скобках с разделением элементов запятыми:
'''
languages = {'python', 'ruby', 'python', 'c'}
print('!!! set не допускае дубликаты\n',languages)

''''
!!! Словари легко перепутать с множествами, 
потому что обе структуры заключаются в фигурные скобки: 
множество не имеет пар «ключ-значение» (в общем случае). 
В отличие от списков и словарей, 
элементы множеств не хранятся в каком-либо определенном порядке.
'''





''''
Вложение

Вложение - структруры, сочетающие множество словарей в списке, списи элементов в словаре, 
а также словари внутрь другого словаря. Выступают мощным механизмом.
'''
print(''''    Вложение''')
print(''''         Список словарей''')

# Пусть требуется создать 3 объекта, образующих совокупность

# Зададим 3 словаря
alien_0 = {'color': 'green', 'points': 5}   #1
alien_1 = {'color': 'yellow', 'points': 10} #2
alien_2 = {'color': 'red', 'points': 15}    #3

aliens = [alien_0, alien_1, alien_2] # Список объектов (словарей)
for alien in aliens:                 # Цикл вывода объектов
    print(alien)


# Моделирование реальных явлений и процессов превышает 3 объекта
# Пусть требуется создать 30 объектов

# Создание пустого списка объектов
aliens = []

# Создание 30 объектов (словарей) с одинаковыми свойствами.
print('\nСоздание 30 объектов (словарей):')
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Вывод первых 5 объектов (словарей):
for alien in aliens[:5]:
    print(alien)
print("...")

# Вывод количества созданных объектов.
print(f"Total number of aliens: {len(aliens)}")





print('    Пример изменения свойств объекта')
''''
Все объекты обладают одинаковыми характеристиками, 
но Python рассматривает каждый словарь как отдельный объект, 
что позволяет изменять атрибуты каждого объекта по отдельности.

Пример изменения свойств объекта
'''

aliens = [] # Создание пустого списка.
# Создание 30 однотипных объектов.
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:5]: # Вывод первых 5 объектов:
    print('первыe 5 объектов: ', alien)
print("...")


# Вывод количества созданных объектов.
print(f"Total number of aliens: {len(aliens)}")



''''
Цикл можно расширить, добавив блок elif 
для превращения желтых объектв в красных — быстрых и имеющих большее числовое значение.
'''

# Создание 30 однотипных объектов.

aliens = [] # Создание пустого списка.
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[0:5]: # Вывод первых 5 объектов:
    print(alien)
print("...")
# Вывод количества созданных объектов.
print(f"Total number of aliens: {len(aliens)}")
''''
КОМЕНТАРИИ к списку словарей 

Все словари в списке должны иметь одинаковую структуру, 
чтобы вы могли перебрать список и выполнить с каждым объектом словаря одни 
и те же операции. 
Хранение словарей в списке достаточно часто встречается тогда, 
когда каждый словарь содержит разные атрибуты одного объекта. 
Например: список словарей, содержащих сведения о пользователях сайта.
'''



print('    Список в словаре')
''''
Список в словаре

Удобно в случаях использования в качестве значения словаря списка значений.
dict{ Ключ:Список[1,2,3], key:list[3,2,1] }

В следующем примере для каждой пиццы сохраняются два вида информации:
 основа и список топпингов. 
 Список топпингов представляет собой значение, связанное с ключом 'toppings'. 
 Чтобы использовать элементы в списке, нужно указать имя словаря и ключ 'toppings', 
 как и для любого другого значения в словаре. 
Вместо одного значения будет получен список топпингов:
'''

# Пример с пиццей.
pizza = {
    'crust': 'thick', # ключ
    'toppings': ['mushrooms', 'extra cheese'], # список значений
    }
# Описание заказа.
print(f"Вы заказзали {pizza['crust']}-хрустящую пиццу " # разбили длин.строку. Закончите строку кавычкой.
    "со следующими начинками:") #  снабдите следующую строку отступом, добавьте открывающую кавычку и продолжите строку.

for topping in pizza['toppings']:
    print("\t" + topping)           # используем +



# Пример с любимыми языками прогр-я друзей
print('\t  Пример с любимыми языками прогр-я друзей')

favorite_languages = {              # несколько языков
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for имя, Языки in favorite_languages.items():
    print(f"\n{имя.title()}'любимые языки:")

    for Языки in Языки: #перебор всех элеменов списка
        print(f"\t{Языки.title()}")
        ''''
        ПРИМЕЧАНИЕ 
        Глубина вложения списков и словарей не должна быть слишком большой. 
        Простое решение - предыдущие примеры.
        '''













''''
Словарь в словаре

Словарь также можно вложить в другой словарь, 
но в таких случаях код быстро усложняется. 
Например, если на сайте есть несколько пользователей с уникальными именами, 
вы можете использовать имена пользователей как ключи в словаре. 

Информация о каждом пользователе при этом хранится в словаре, 
который используется как значение, связанное с именем.

В следующем примере о каждом пользователе хранится три вида информации: 
имя, 
фамилия и 
место жительства. 

Чтобы получить доступ к этой информации, переберите имена пользователей 
и словарь с информацией, связанной с каждым именем:
'''
print('    Словарь в словаре')


users = {                     # определяется словарь с именем users
    'aeinstein': {            # ключ для пользователя aeinstein
        'first': 'albert',    # значения для пользователя aeinstein
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {               # ключ для пользователя mcurie
        'first': 'marie',     # значения для пользователя mcurie
        'last': 'curie',
        'location': 'paris',
        },
    'Артемон': {
        'first':'Артем',
        'last' : 'Рожков',
        'location' : 'Челябинск',
        }
    }
'''
В процессе перебора словаря users Python сохраняет каждый ключ 
в переменной username, а словарь, связанный с каждым именем пользователя, 
сохраняется в переменной user_info.
'''
for username, user_info in users.items():
    print(f"\nUsername: {username}")  # Внутри основного цикла в словаре выводится имя пользователя

    """
    Начинается работа с внутренним словарем. 
    Переменная user_info, содержащая словарь с информацией о пользователе, 
    содержит три ключа: 'first', 'last' и 'location'. 
    Каждый ключ используется для построения аккуратно отформатированных данных
    """

    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


''''
Примечение. 
Обратите внимание на идентичность структур словарей всех пользователей 
в приведенном примере. 
Наличие единой структуры упрощает работу с вложенными словарями. 
Если словари разных пользователей будут содержать разные ключи, 
то код в цикле for заметно усложнится.
'''

print('    \n\tИнфо из udemy \n\t Вытащим все ключи из словаря, переведем их в список')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'artem' : 'python'
    }
keys = favorite_languages.keys()
print('Ключи словаря:\n', keys)

keys_list = list(favorite_languages.keys())
print('Ключи в списке:\n', keys_list)
print(type(keys_list))

# или тоже получаем список, но отсортированный по алфавиту
print('Список по алфавиту при помощи Sorted: ', sorted(favorite_languages.keys()))

# проверим есть ли такой ключ (имя) в словаре функция in и not in

print('artem' in favorite_languages)
'Есть ли artem в словаре favorite_languages'

print('Если alisa нет в словаре - True:', 'alisa' not in favorite_languages)
'Отсутствует ли alisa в словаре favorite_languages'

''''
Что бы также работать со значениями есть функция values
также можно переворачивать в лист, сортировать по возрастанию
проверять на присутствие
'''

# Также можно создать поверхностную копию (внутренняя репрезентация объектов скопирована не будет)
print('Также можно создать поверхностную копию (внутренняя репрезентация объектов скопирована не будет)')
favorite_languages_copy = favorite_languages.copy()
print(favorite_languages_copy)

# Что бы удалить пару по ключу функция pop
print('до удалениея', favorite_languages)
favorite_languages.pop('sarah')
print('после удаления:', favorite_languages)

# Что бы удалить с конца -> popitem()
print('\nЧто бы удалить с конца')
print(favorite_languages.popitem())
'''' Распечали то, что удаляем'''

print('Распечатали словарь после удаления:', favorite_languages)

# подсчитаем количество пар len
print('\nподсчитаем количество пар len')
print(len(favorite_languages))

# проверка на присутствие определенного имени
# и в случае отсутствия автоматически добавляет этот ключ со значением none -> setdefault


favorite_languages.setdefault('Бабабакин')
print(favorite_languages)


# Словари. Генераторы словарей
print('\tГенераторы словарей')

# 1. Сгенерировать словарь на основе заданного выражения
# Генерируются пары (ключ: значение) = (i: 5*i)
A = { i: i*5 for i in [10,20,30,40] }
print('A', A) # {10: 50, 20: 100, 30: 150, 40: 200}

# 2. Сгенерировать словарь по итерируемому объекту (строке)
print('\tСгенерировать словарь по итерируемому объекту (строке)')
s = 'Hello'
B = { sym: sym*3 for sym in s } # пара (sym:sym*3)
print('B=', B) # {'H': 'HHH', 'e': 'eee', 'l': 'lll', 'o': 'ooo'}

numbers = [ 15, 25, 30 ]
C = { num: str(num) for num in numbers }
print('C=', C) # {15: '15', 25: '25', 30: '30'}



# 3. Инициализация словаря из списка ключей
print('\tИнициализация словаря из списка ключей')
# Заполнить список ключей значением, введенным с клавиатуры

value = int(input('Input value: '))
listKeys = [ 1, 2, 3, 4 ]
D = { lk:value for lk in listKeys }
print(D)

# Заполнить список ключей значением None
value = None
listKeys = [ 'a', 'b', 'c' ]
E = { lk:value for lk in listKeys }
print(E) # {'a': None, 'b': None, 'c': None}

# 4. Сгенерировать словарь с использованием функции zip()
WMonths = [ 'Dec', 'Jan', 'Feb']
NumMonths = [ 12, 1, 2 ]
F = { nm:wm for (nm,wm) in zip(NumMonths,WMonths) }
print(F) # {12: 'Dec', 1: 'Jan', 2: 'Feb'}






