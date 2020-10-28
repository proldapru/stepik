m1, m2 = [], []
# Ввод первой матрицы, заполнение нулями второй матрицы
while True:
	l = input()
	if l == 'end': break
	m1.append([int(i) for i in l.split()])
	m2.append([0 for i in l.split()])

# Расчёт второй матрицы
rows, cols = len(m1), len(m1[0])
for r in range(rows):
	for c in range(cols):
		m2[r][c] += m1[r-1][c] + m1[r + 1 - rows][c] + m1[r][c-1] + m1[r][c + 1 - cols]
# Вывод
for r in m2:
	print(*r)

