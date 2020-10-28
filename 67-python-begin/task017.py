a, b, c, d = int(input()), int(input()), int(input()), int(input())

print(' ' , end='')
for i in range(c, d+1):
	print('\t' + str(i), end='')
print()
for i in range(a, b+1):
	print(i, end='')
	for j in range(c, d+1):
		print('\t' + str(i*j), end='')
	print()