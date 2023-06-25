def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            # Проверяем, бьют ли ферзи друг друга
            if (queens[i][0] == queens[j][0] or  # Проверка горизонтали
                queens[i][1] == queens[j][1] or  # Проверка вертикали
                abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1])):  # Проверка диагонали
                return False
    return True

queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]

result = check_queens(queens)

if result:
    print("Ферзи не бьют друг друга")
else:
    print("Ферзи бьют друг друга")