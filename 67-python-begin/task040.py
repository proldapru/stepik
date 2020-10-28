from requests import get
with open('input40.txt') as inf, open('output40.txt','w') as ouf:
	url = get(inf.readline().strip()).text
	#url = '843785.txt'
	while True:
		url = get('https://stepic.org/media/attachments/course67/3.6.3/' + url).text
		if url[0:2] == 'We': break
		print(url)
	print(url, file=ouf)
