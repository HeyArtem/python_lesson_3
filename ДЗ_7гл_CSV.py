# ДЗ после 7 главы. Создать CSV фаил


import csv
''''

функция csv.reader -> Чтение в тип list
функция csv.writer -> Запись из листа
класс csv.Dictwriter -> Класс, запись в обьект типа словарь
класс csv.DictReader -> Класс, чтение в обьект типа словарь

'''

car_data = [['brand', 'model', 'volume', 'fuel'], ['Kia', 'Rio', '1,4', '8'], ['Reno', 'Fluence', '1,6', '8,5'], ['Volkswagen', 'Polo', '1,5', '8,7'], ['Hyundai', 'solaris', '1,4', '7,8']]



with open('data_auto.csv', 'w', newline='') as f: # newline-> делает, что бы запись делалась каждую строку, а не через одну
    writer = csv.writer(f, delimiter = '>')  # Разделитель(delimiter), по умолчанию ','
    writer.writerows(car_data)
print('Writing complete!')

print(' * ')

with open('data_auto.csv') as f:
    читаю = csv.reader(f, delimiter = '>')
    for row in читаю:
        print(row)

print(' * ')

data_school_dict = [{'Name':'Dima', 'age':'10', 'Grade':'A'},
               {'Name':'Vasia', 'age':'11', 'Grade':'C'},
               {'Name':'Hasim', 'age':'13', 'Grade':'f'},
               {'Grade':'B', 'Name':'Zoy', 'age':'14'}]
fieldnames = ['Name', 'age', 'Grade']
with open('Список_учеников.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, delimiter = '-', fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(data_school_dict)):
        writer.writerow(data_school_dict[i])
print('   Writing Список_учеников.csv complete!')

print(' * ')

with open ('Список_учеников.csv') as f:
    reader = csv.DictReader(f, delimiter = '-')
    for row in reader:
        print(row) #  У меня выведется dict, у преподавателя tuple   ( [('Name','Dima'),('age','10')] )


print(' * ')

import pandas as pd
проба_pandas_from_csv = pd.read_csv('Список_учеников.csv', sep = '-')
print(type(проба_pandas_from_csv))
print(проба_pandas_from_csv)


