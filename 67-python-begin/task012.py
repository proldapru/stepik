n = int(input())
out = str(n) + ' программист'

m100 = n % 100
m10 = n % 10
if m10==0 or m10>=5 or 11<=m100<=14: out += 'ов'
elif 2<=m10<=4: out += 'а'

print(out)
