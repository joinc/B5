# -*- coding: utf-8 -*-

from random import randint


######################################################################################################################

#Игровое поле (playing field)
pf = [
    '-','-','-',
    '-','-','-',
    '-','-','-'
]

# Победные линии (winning lines)
winning_lines = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8],
	[0, 3, 6],
	[1, 4, 7],
	[2, 5, 8],
	[0, 4, 8],
	[2, 4, 6]
]

human = True
step = 0
 
 
######################################################################################################################

# Проверка на выигрыш
def check_win():
	winner = False
	for line in winning_lines:
		if pf[line[0]] == 'X' and pf[line[1]] == 'X' and pf[line[2]] == 'X':
			winner = 'X'
		if pf[line[0]] == 'O' and pf[line[1]] == 'O' and pf[line[2]] == 'O':
			winner = 'O'
	if winner:
		print(f'\nПобедил {winner}!')
		raise SystemExit(1)
	else:
		if step == 9:
			print(f'\nНичья!')
			raise SystemExit(1)


######################################################################################################################

# Увеличение номера хода
def next_step():
    global step
    step += 1

######################################################################################################################

# Функция отображения игрового поля
def print_playing_field():
    print('  0 1 2')
    for row in range(0, 3):
        print(f'{row} {pf[3 * row + 0]} {pf[3 * row + 1]} {pf[3 * row + 2]}')
    check_win()
    next_step()


######################################################################################################################

# Возвращает выигрышный ход, если он есть
def get_move(symbol):
	move_index = False
	for index in range(0, 9):
		if pf[index] == '-':
			for line in winning_lines:
				if pf[line[0]] == symbol and pf[line[1]] == symbol and line[2] == index:
					move_index = index
				if pf[line[0]] == symbol and line[1] == index and pf[line[2]] == symbol:
					move_index = index
				if line[0] == index and pf[line[1]] == symbol and pf[line[2]] == symbol:
					move_index = index
	return move_index


######################################################################################################################


def choose_move():
	# Проверяем выигрышную комбинацию компьютера
	move_index = get_move(symbol='O' if human else 'X')
    # Проверяем выигрышную комбинацию человека
	if not move_index:
		move_index = get_move(symbol= 'X' if human else 'O')
	while not move_index:
		random_index = randint(0, 8)
		if pf[random_index] == '-':
			move_index = random_index
	return move_index

		
######################################################################################################################

# Перевод координат в индекс игрового поля
def coords_to_index(row, col):
    return 3 * row + col


######################################################################################################################

# Перевод индекс игрового поля в координаты
def index_to_coords(index):
	coords = ['0 0', '0 1', '0 2', '1 0', '1 1', '1 2', '2 0', '2 1', '2 2']
	return coords[index]


######################################################################################################################

# Ход компьютера
def move_computer():
	if step == 1:
		move_index = 0
	elif step == 2:
		move_index = 4 if pf[4] == '-' else 0
	elif step == 3:
		if pf[4] == 'O':
			move_index = 8
		elif pf[3] == 'O' or pf[3] == 'O':
			move_index = 2
		else:
			move_index = 6
	else:
		move_index = choose_move()
	pf[move_index] = 'O' if human else 'X'
	print(f'\nХод №{step}. Ход компьютера - [{index_to_coords(move_index)}].')
	print_playing_field()


######################################################################################################################

# Ход человека
def move_human():
	is_correct = False
	while not is_correct:
		coords = input('Введите координаты хода, две цифры через пробел, строку и столбец (0, 1 или 2): ').split()
		if len(coords) > 1:
			row, col = int(coords[0]), int(coords[1])
			index = coords_to_index(row=row, col=col)
			if row in range(0, 3) and col in range(0, 3):
				if (pf[index] == '-'):
					pf[index] = 'X' if human else 'O'
					is_correct = True
				else:
					print(f'Ячейка [{row} {col}] не пустая и уже занята.')
			else:
				print('Вы ввели не существующие координаты хода.')	
		else:
			print('Вы ввели не достаточное количество координат хода.')
	print(f'\nХод №{step}. Ход человека - [{row} {col}].')
	print_playing_field()


######################################################################################################################


def main():
	symbol = False
	global human
	while symbol not in ['X', 'x', 'O', 'o', '0']:
		symbol = input('Выберите каким символом Вы будете ходить - X или O (X ходит первым): ')
	if symbol in ['X', 'x']:
		print('Вы выбрали X. Вы ходите первым.')
		print_playing_field()
	else:
		print('Вы выбрали O. Первым ходит компьютер.')
		human = False
		next_step()
		move_computer()
	while True:
		move_human()
		move_computer()


######################################################################################################################


if __name__ == '__main__':
    main()


######################################################################################################################
