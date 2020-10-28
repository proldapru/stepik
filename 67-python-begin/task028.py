n, m = int(input()), [[]]

# Формирование почти пустой матрицы
m[0] = [i+1 for i in range(n)] # первая строка заполнена сразу
for i in range(n - 1): # в остальных строках нули
	m.append([0] * n)

# Заполнение матрицы
counter, goal, steps, row, col = n, n * n,  n, 0, n - 1

while counter < goal:
	for move in range(4):
		if not move % 2:
			steps -= 1
		for i in range(steps):
			if move==0: row += 1
			if move==1: col -= 1
			if move==2: row -= 1
			if move==3: col += 1
			counter += 1
			m[row][col] = counter	

# Вывод матрицы
for i in m:
	print(*i)