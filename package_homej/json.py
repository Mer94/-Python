#Функция read_json_file считывает данные из файла JSON и возвращает их в виде словаря или списка

import json

def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

#Функция write_json_file записывает данные в файл JSON

def write_json_file(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)