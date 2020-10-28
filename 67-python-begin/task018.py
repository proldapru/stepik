a, b, c, s = int(input()), int(input()), 0, 0

for i in range(a, b+1):
	if i % 3 == 0:
		c += 1
		s += i
print(s / c)