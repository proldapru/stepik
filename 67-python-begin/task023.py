s = sorted([int(i) for i in input().split()])
n, c, t = s[0], 1, '';

for i in s[1:]:
	if n==i:
		c+=1
	else:
		if c>1: t += str(n) + ' '
		n = i
		c = 1

if c>1: t += str(n) + ' '

print(t[0:-1])
