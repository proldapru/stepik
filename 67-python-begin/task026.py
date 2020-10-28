s, n = [int(i) for i in input().split()], int(input())
if not s.count(n):
	print('Отсутствует')
else:
	s2 = []
	for i in range(len(s)):
		if s[i] == n:
			s2.append(i)
	print(*s2)

