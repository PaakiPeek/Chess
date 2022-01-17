# Создание игровой доски, где "." - белая клетка, "*" - черная клетка.
symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# Словарь с фигурами и их положением на доске
figures = {'ph1': ['2a', '7a'], 'ph2': ['2b', '7b'], 'ph3': ['2c', '7c'], 'ph4': ['2d', '7d'], 'ph5': ['2e', '7e'],
           'ph6': ['2f', '7f'], 'ph7': ['2g', '7g'], 'ph8': ['2h', '7h'], 'K': ['1d', '8d'], 'Q': ['1e', '8e'],
           'RL': ['1a', '8a'], 'RR': ['1h', '8h'], 'HL': ['1b', '8b'], 'HR': ['1g', '8g'], 'EL': ['1c', '8c'],
           'ER': ['1f', '8f']}
log_game = []
game = True
print('Начнем игру!')
Player_count = 0

while game:
    l = [['.'] * 9 for i in range(9)]
    for row in range(9):
        for col in range(9):
            # Выстраиваем по горизонтале четные
            if row != 8:
                if row % 2 == 0:
                    if col % 2 != 0:
                        l[row][col] = '*'
            else:
                if col < 8:
                    l[row][col] = symbols[col]
                else:
                    l[row][col] = ''
            # Выстраиваем по горизонтале не четные
            if col != 8:
                if row % 2 != 0:
                    if col % 2 == 0:
                        l[row][col] = '*'
            else:
                if row < 8:
                    l[row][col] = str(9 - (row + 1))
                else:
                    l[row][col] = ''

    # Создание вспомогательной таблицы
    l2 = [['.'] * 8 for i in range(8)]
    for row in range(8):
        for col in range(len(l2[row])):
            l2[col][row] = str(9 - (col + 1))
    for row in range(8):
        for col in range(len(l2[row])):
            l2[row][col] += symbols[col]

    for row in range(8):
        for col in range(len(l2[row])):
            for figure in figures:
                if l2[row][col] == figures[figure][0]:
                    l2[row][col] = str(figure).upper()
                    l[row][col] = str(figure[0]).upper()
                if l2[row][col] == figures[figure][1]:
                    l2[row][col] = str(figure).lower()
                    l[row][col] = str(figure[0]).lower()

    for row in range(9):
        for col in range(len(l[row])):
            print(l[row][col].ljust(8), end='')
        print()
    print()

    Player_figure = input('Выберете позицию фигуры: ')
    Player_step = input('Выберете клетку для хода: ')
    for figure in figures:
        if Player_count % 2 == 0:
            if Player_figure == figures[figure][0]:
                figures[figure][0] = Player_step
        else:
            if Player_figure == figures[figure][1]:
                figures[figure][1] = Player_step

    if Player_step == figures['K'][0] or Player_step == figures['K'][1]:
        game = False
        print('Поделил игрок: ' + str(Player_count//2 + 1))

    log_game.append(str(Player_count) + ': ' + Player_figure + ' - ' + Player_step)
    print(*log_game)
    Player_count += 1
