#Функция read_csv_file считывает данные из файла CSV и возвращает их в виде списка строк или списков

import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

#Функция write_csv_file записывает данные в файл CSV.

def write_csv_file(data, file_path):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)