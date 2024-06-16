# -*- coding: utf-8 -*-

import os
import time

directory = 'C:\\Users\\serge\\PycharmProjects\\Homeworks\\module_7_filework_and_formatted_output\\OS_windows_file'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time},',
              f'Родительская директория: {parent_dir}')
