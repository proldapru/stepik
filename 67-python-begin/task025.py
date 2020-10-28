n = int(input())
s = []
for i in range(1, n+1):
	for j in range(i):
		s.append(i)
		if len(s) == n: break
	if len(s) == n: break
print(*s)

