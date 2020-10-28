d = {}

with open('input45.txt') as inf, open('output45.txt','w') as ouf:
	for line in inf:
		data = line.strip().split('\t')
		d.setdefault(data[0], [0, 0])
		d[data[0]][0] += int(data[2])
		d[data[0]][1] += 1
	print(d)
	for i in range(1, 12):
		i = str(i)
		if i in d: print(i, d[i][0]/d[i][1], file=ouf)
		else: print(i, '-', file=ouf)


''' Решение со степик

c = {str(i):[0]*2 for i in range(1,12)}
for l in open('in'):
    s = l.strip().split()[::2]
    c[s[0]] = [c[s[0]][0] + int(s[1]), c[s[0]][1] + 1]
[print(k + ' ', v[0]/v[1] if v[0] else '-') for k, v in c.items()]

'''


''' Решение со степик

import pandas as pd

df = pd.read_table('C:\\Users\\User\\Desktop\\py_course\\dataset_3380_5.txt', header=None, sep=r'\s{1,}')
print(df.groupby(0).mean())

'''