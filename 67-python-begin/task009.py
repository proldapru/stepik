x, y, op = float(input()), float(input()), input()
if op in ['/', 'div', 'mod'] and y==0.0:
	print('Деление на 0!')
elif op=='+':
	print(x + y)
elif op=='-':
	print(x - y)
elif op=='/':
	print(x / y)
elif op=='*':
	print(x * y)
elif op=='mod':
	print(x % y)
elif op=='pow':
	print(x ** y)
elif op=='div':
	print(x // y)
else:
	print('Unknown operation')

