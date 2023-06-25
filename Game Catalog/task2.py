# import task
#
# def new_puzzle(puzzles: dict, try_count: int):
#     for key, val in puzzles.items():
#         try_count_1 = task.puzzle(key, val, try_count)
#         if try_count_1:
#             print(f'Угадано за {try_count_1} попыток')
#         else:
#             print("Не угадали")

import task

_ANSWEARS = dict()

def new_puzzle(puzzles: dict, try_count: int):
    for key, val in puzzles.items():
        try_count_1 = task.puzzle(key, val, try_count)
        if try_count_1:
            _ANSWEARS[key] = f'Угадано за {try_count_1} попыток'
            print(f'Угадано за {try_count_1} попыток')
        else:
            _ANSWEARS[key] = "Не угадали"
            print("Не угадали")

def show_result():
    print(*(f'{key} - {val}\n' for key, val in _ANSWEARS.items()))