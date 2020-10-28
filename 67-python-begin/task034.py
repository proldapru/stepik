input_file = open('input34.txt')
s1 = input_file.readline()
input_file.close()

s2, char, number = '', s1[0], s1[1]
n = 0
for i in s1[2:]:
#	print(i, s2)
#	n+=1
#	if n == 10: break
	if i < 'A':
		number += i
	else:
		s2 += char * int(number)
		char = i
		number = ''
s2 += char * int(number)
print(s2)


output_file = open('output34.txt', 'w')
print(s2, file=output_file)
output_file.close()

''' Решение со Степика
with open('dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()
i = 0
while i < len(s):
    j = i + 1
    while j < len(s) and s[j].isdigit():
        j += 1
    print(s[i] * int(s[i+1:j]), end='')
    i = j

Первый символ - гарантированно буква.
Перебираем все последующие, пока они цифровые или пока не достигнут конец строки.
После внутреннего цикла j либо указывает на следующую букву, либо на конец строки. В обоих случаях между s[i] и s[j] - цифры, составляющие нужное нам число повторов символа s[i].

Печатаем символ нужное число раз, присваиваем i индекс следующей буквы для новой итерации цикла.

'''

''' Решение со Степика
s, d = input(), []
for i in s:
    if not i.isdigit(): d.append(i)
    else: d[-1] += i
print(*[i[0]*int(i[1:]) for i in d], sep='')
'''