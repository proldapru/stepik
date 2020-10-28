input_file = open("input35.txt", 'r')
l = input_file.read().replace('\n', ' ').lower().split()
input_file.close()

#l = 'abc a bCd bC AbC BC BCD bcd ABC'.lower().split()
word, cnt = '', 0
for i in set(l):
	if l.count(i) > cnt:
		cnt = l.count(i)
		word = i
	elif l.count(i) == cnt and i < word:
		word = i
print(word, cnt)

output_file = open('output35.txt', 'w')
print(word, cnt, file=output_file)
output_file.close()


''' Решение со Степика

with open('dataset_3363_3.txt') as inf, open('MostPopularWord.txt','w') as ouf:
    maxc = 0
    s = inf.read().lower().strip().split()
    s.sort()
    for word in s:
        counter = s.count(word)
        if counter > maxc:
            maxc = counter
            result_word = word
    ouf.write(result_word +' ' + str(maxc))

'''

''' Решение со Степика с фунцией из модуля

from collections import Counter

with open('Bible.txt', 'r') as file:
    words = [i.lower() for i in file.read().split()]

most_common = Counter(words).most_common(1)[0]
print(*most_common)

'''

''' Решение со Степика без метода .count()

s, d, m, w = str(), dict(), 0, str()
with open("dataset_3363_3.txt", "r") as f:
    s = f.read().lower().strip().split()
s.sort()
for word in s:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for word in d:
    if d[word] > m:
        m = d[word]
        w = word

'''