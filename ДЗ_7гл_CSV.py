# ДЗ после 7 главы. Создать CSV фаил

''''

функция csv.reader -> Чтение в тип list
функция csv.writer -> Запись из листа
класс csv.Dictwriter -> Класс, запись в обьект типа словарь
класс csv.DictReader -> Класс, чтение в обьект типа словарь

'''

car_data = [['brand', 'model', 'volume', 'fuel'], ['Kia', 'Rio', '1,4', '8'], ['Reno', 'Fluence', '1,6', '8,5'], ['Volkswagen', 'Polo', '1,5', '8,7']]

with open('data_auto.csv', 'w') as f:
    writer = csv.writer(f)  # Разделитель(delimiter), по умолчанию ','
    writer.writerrows(car_data)
print('Writing complete!')
