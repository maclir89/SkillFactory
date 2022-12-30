def text_p(a):  # Функция форматирования вывода текста, где каждая строка помещена в список
    for i in range(len(a)):
        print("{:-^30}".format(a[i]))


greating = ['', 'Давайте сыграем в игру', 'Крестики-нолики', '', 'Формат ввода х у или xy', 'х - номер строки',
            'у - номер столбца', '!!!Удачи!!!', '']

text_p(greating)

field = [[' '] * 3 for i in range(3)]  # Инициализация поля


def field_print():  # Функция вывода поля на печать
    print(f'   | 1 | 2 | 3 |')
    for i, r in enumerate(field):
        print(f' {i + 1} | {" | ".join(r)} |')


def question():  # Функция ввода и проверка условий
    while True:
        str = input("Введите ХY: ")
        cord = []
        for i in range(len(str)): cord.append(str[i])

        if len(cord) != 2 and len(cord) != 3:
            print("Нужны 2 координаты")
            continue

        if len(cord) == 3 and cord[1] != " ":
            print("Координаты могут быть разделены только пробелом")
            continue

        if len(cord) == 3 and cord[1] == " ":
            cord.pop(1)

        x, y = cord

        if not (x.isdigit()) or not (y.isdigit()):
            print("Нужно вводить цифры")
            continue
        x, y = int(x), int(y)

        if not 1 <= x <= 3 or not 1 <= y <= 3:
            print("Нужно вводить цифры от 1 до 3")
            continue

        if field[x - 1][y - 1] != " ":
            print("Клетку уже заняли")
            continue
        return x, y


def check_win():  # Функция проверки игры на выигрышную комбинацию
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for cord in win_cord:
        x_o = []
        for i in cord:
            x_o.append(field[i[0]][i[1]])

        if x_o == ["X", "X", "X"]:
            field_print()
            print("!!!Выиграл Х!!!")
            return True
        if x_o == ["0", "0", "0"]:
            field_print()
            print("!!!Выиграл 0!!!")
            return True
    return False


count = 0

while True:

    count += 1

    field_print()

    if count % 2 == 1:
        print("Ходит Х")
    else:
        print("Ходит 0")

    x, y = question()

    if count % 2 == 1:
        field[x - 1][y - 1] = "X"
    else:
        field[x - 1][y - 1] = "0"

    if check_win():
        break

    if count == 9:
        field_print()
        print("Увы, ничья")
        break
