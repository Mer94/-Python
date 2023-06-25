def puzzle(text: str, answears: list[str], try_count:int) -> int:
    print(text)
    count_trying = 1

    while count_trying <= try_count:
        answear = input("Что это?")
        if answear in answears:
            break
        if count_trying != try_count:
            print('Не угадал')
        count_trying +=1
    else:
        count_trying = 0

    return count_trying