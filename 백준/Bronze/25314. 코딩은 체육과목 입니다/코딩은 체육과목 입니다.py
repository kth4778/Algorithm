a=int(input())
b=[]
o=a%4
p=int(a/4)
if o==0:
    for i in range(p):
        b.append('long')
print(' '.join(b),'int')