s1, s2 = 0, 0
while True:
	n = int(input())
	s1 += n
	s2 += n * n
	if s1 == 0: break
print(s2)
