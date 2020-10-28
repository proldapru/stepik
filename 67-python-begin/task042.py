data, cipher1, cipher2 = [], {}, {}
#for i in ['abcd', '%*7#', 'aabbcacdadd', '7%%#77#*7*']: data.append(i)
for i in range(4): data.append(input())
for k, v in zip(list(data[0]), list(data[1])):
    cipher1[k] = v
    cipher2[v] = k
print(''.join([cipher1[i] for i in data[2]]))
print(''.join([cipher2[i] for i in data[3]]))

''' Решение со степика

a,b,c,d=input(),input(),input(),input()
print(''.join(b[a.index(i)] for i in c))
print(''.join(a[b.index(i)] for i in d))

'''