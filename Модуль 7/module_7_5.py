import os
import time

path = r'C:\Users\Владислав\Desktop\Программирование\UrbanUniversity\Модуль 7\module_7_5'
for root, dirs, files in os.walk(path):
    for file in files:
        filepath = os.path.join(file, path)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

# Обнаружен файл: module_7_5.py,
# Путь: C:\Users\Владислав\Desktop\Программирование\UrbanUniversity\Модуль 7\module_7_5,
# Размер: 0 байт, Время изменения: 29.07.2024 20:51,
# Родительская директория: C:\Users\Владислав\Desktop\Программирование\UrbanUniversity\Модуль 7
