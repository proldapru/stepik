direction, x, y = {'север':[0, 1], 'юг':[0, -1], 'восток':[1, 0], 'запад':[-1, 0]}, 0, 0
for _ in range(int(input())):
	cur_dir, path = input().lower().split()
	x += direction[cur_dir][0] * int(path)
	y += direction[cur_dir][1] * int(path)
print(x, y)

''' Решение со Степика

n=int(input())
d={'север':0,'запад':0,'юг':0,'восток':0}
for i in range(n):
    x=input().split()
    d[x[0]]+=int(x[1])
print(d['восток']-d['запад'], d['север']-d['юг'])

'''