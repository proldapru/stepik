l, d = input().lower().split(), {}

for i in l:
	d[i] = d.get(i, 0) + 1

for k, v in d.items():
	print(k, v)

''' Решение на Степике

s = input().lower().split()
for i in set(s):
    print(i, s.count(i))

'''

''' Еще решение со Степика

text = input().lower().split()
d = { i : text.count(i) for i in text  }
for key, value in d.items():
    print(key, value, end='\n')

'''