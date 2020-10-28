sum = 0
getZero = False

while not getZero:
	n = int(input())
	sum += n
	getZero = n==0

print(sum)
