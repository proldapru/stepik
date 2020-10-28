a, b = int(input()), int(input())
p = 0;

if a<b: a, b = b, a

if a==b or a % b == 0:
	p = a
else:
	p = i = a * b
	while i>a:
		if not i % a and not i % b: p = i
		i -= 1
print(p)
