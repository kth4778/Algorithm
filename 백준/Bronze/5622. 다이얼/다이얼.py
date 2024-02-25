a = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
b = {i:index+2 for index,w in enumerate(a) for i in w}
c=list(input().upper())
d=[b[c[i]] for i in range(len(c))]
print(sum(d)+len(c))