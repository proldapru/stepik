f, a = input(), float(input())
if f=='круг': print(3.14 * a ** 2)
elif f=='прямоугольник':
	b = float(input())
	print(a * b)
else:
	b, c = float(input()), float(input())
	p = (a + b +c) / 2
	print((p*(p-a)*(p-b)*(p-c))**0.5)

