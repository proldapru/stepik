def modify_list(lst):
	for i in range(len(lst)-1, -1, -1):
		if not lst[i] % 2: lst[i] //= 2
		else: del lst[i]
		#print(i)

'''
Вариант со степика:

def modify_list(l):
    l[:] = [i//2 for i in l if not i % 2]

'''


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]