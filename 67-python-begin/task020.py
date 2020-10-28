string, newString = input(), ''
curChar = string[0]
curCharCount = 1;
for i in string[1:]:
	if i==curChar:
		curCharCount += 1
	else:
		newString += curChar + str(curCharCount)
		curChar = i
		curCharCount = 1
print(newString + curChar + str(curCharCount))
