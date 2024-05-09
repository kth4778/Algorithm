a=int(input())
strin=[]
for _ in range(a):
    strin.append(list(input()))
for string in strin:
	result=[]
	for char in  string:
		if char=='(':
			result.append(char)
		elif char==')' and result and result[-1]=='(':
			result.pop()
		else:
			print('NO')
			break
	else:
		if not result:
			print('YES')
		else:
			print('NO')