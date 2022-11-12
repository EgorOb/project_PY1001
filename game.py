from typing import List, Union, Tuple


def init_field(size: int, empty_cell: Union[str, None]) -> List[List]:
    """
    Возвращает пустое поле
    :param size: параметр размера поля
    :param empty_cell: параметр заполнения пустой ячейки
    :return: поле в виде списка списков
    """
    field = []
    for row in range(size):
        field.append([empty_cell]*size)

    # field = []
    # for row in range(size):
    #     tmp = []
    #     for _ in row:
    #         tmp.append(empty_cell)
    #     field.append(tmp)

    return field, 1


def draw_field(field: List[List]) -> None:
    """

    :param field:
    :return:
    """
    for row in field:
        for cell in row:
            print(f"|{cell}", end="")
        print("|")


def get_int_val(text, border=None):
    """
    Возвращаем целое число с проверками
    :param text:
    :param border:
    :return:
    """
    while True:
        val = input(text)
        try:
            val = int(val)
        except ValueError:
            print("Должно быть целое число")
            continue
        if border is not None:
            if not 0 <= val <= border:
                print(f"Значение должно быть в интервале (0, {border})")
                continue
        return val


def get_char(text: str, req_list: List) -> str:
    """
    Проверка что символ находится среди требуемых
    :param text:
    :param req_list: список требуемых символов
    :return:
    """
    while True:
        val = input(text)
        if val not in req_list:
            print(f"Значение должно быть из списка {req_list}")
            continue
        return val


def get_index_from_step(field: List[List], size: int) -> Tuple[int, int]:
    """
    Функция для получения индексов куда нужно ходить
    :param field:
    :param size:
    :return:
    """
    while True:
        index_row = get_int_val("Введи индекс для строки\n", size - 1)
        index_col = get_int_val("Введи индекс для столбца\n", size - 1)
        if field[index_row][index_col] != " ":
            print("Ячейка занята")
            continue
        return index_row, index_col


def set_player_to_field(field, current_player, index_row, index_col):
    """

    :param field:
    :param current_player:
    :param index_row:
    :param index_col:
    :return:
    """
    field[index_row][index_col] = current_player
    return field


def change_player(player):
    """

    :param player:
    :return:
    """
    new_player = "X" if player == "0" else "0"

    # if player == "0":
    #     new_player = "X"
    # else:
    #     new_player = "0"

    return new_player


def is_win(field):
    """

    :param field:
    :return:
    """
    # Если есть выигрышный момент для любого игрока, т.е. есть последовательность из n одинаковых символов
    # и эта последовательность не пустой элемент, то возвращаем True
    # А если мы не нашли ни один выигрышный момент, то возвращаем False

    return False


def game(field, size, player):
    # Функция запуска игры
    current_player = player # игрок
    count_step = 0 # счетких текущего хода
    draw_field(field) # отрисовали поле
    while count_step < size*size:
        print(f"Ставит игрок {current_player}")
        index_row, index_col = get_index_from_step(field, size) # получили координаты для хода
        field = set_player_to_field(field, current_player, index_row, index_col) # поставили игрока на поле
        count_step += 1 # обновили счетчик ходов
        draw_field(field) # отрисовали поле
        if is_win(field): # Проверка выигрыша
            print(f"Выиграл игрок {current_player}")
            return current_player # break
        current_player = change_player(current_player)  # смена игрока

    # if count_step == size*size:
    #     print("Ничья")

    print("Ничья")
    return None


def app():
    """
    Запуск приложения
    :return:
    """
    size = get_int_val("Введи размер поля\n")  # Определяем размер поля (можно с использованием input())
    empty_cell = " "
    field = init_field(size, empty_cell)
    player = get_char("Кто будет играть первым?\n", req_list=["X", "0"])  # Определяем кто первым играет (можно с использованием input())
    who_player = get_char(f"C кем играем? {['h', 'c']}\n", req_list=['h', 'c'])  # С кем играем (1, 2), ("human", "comp"), ("h", "c")
    if who_player == "h":
        stats = game(field, size, player)
    else:
        print("В разработке")
        print("Хотите сыграть с человеком?")


if __name__ == "__main__":
    app()
