from requests import get
with open('input39.txt') as inf, open('output39.txt','w') as ouf:
	url = inf.readline().strip()
	r = get(url)
	print(len(r.text.splitlines()), file=ouf)
