sum_list, lines_count = [0, 0, 0], 0

with open('input36.txt') as inf, open('output36.txt','w') as ouf:
	for line in inf:
		lines_count += 1
		marks = [int(i) for i in line.split(';')[1:]]
		for i in range(3):
			sum_list[i] += marks[i]
		print(sum(marks)/3, file=ouf)
	print(sum_list[0]/lines_count, sum_list[1]/lines_count, sum_list[2]/lines_count, file=ouf)