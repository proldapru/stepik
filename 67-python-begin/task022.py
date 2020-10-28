s = [int(i) for i in input().split()]
n = len(s)
if n==1:
	print(s[0])
else:
	t = ''
	for i in range(n):
		if i==0: t += str(s[1] + s[-1]) + ' '
		elif i==n-1: t += str(s[0] + s[-2]) + ' '
		else: t += str(s[i - 1] + s[i + 1]) + ' '
	print(t[0:-1])