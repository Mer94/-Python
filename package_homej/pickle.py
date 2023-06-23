import pickle

#Функция read_pickle_file считывает данные из файла pickle и возвращает их.

def read_pickle_file(file_path):
    with open(file_path, "rb") as file:
        data = pickle.load(file)
    return data

#Функция write_pickle_file записывает данные в файл pickle.

def write_pickle_file(data, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(data, file)