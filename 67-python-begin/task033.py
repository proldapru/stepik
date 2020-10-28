n, d = int(input()), {}
for i in range(n):
	x = int(input())
	if not x in d:
		d[x] = f(x)
	print(d[x])

''' Решение со Степика
a=[int(input()) for i in range(int(input()))]
b={x:f(x) for x in set(a)}
for i in a:
    print(b[i])
'''