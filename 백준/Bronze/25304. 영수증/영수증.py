a,b=map(int,(input(),input()))
o=[]
for i in range(b):
    q,w=map(int,input().split())
    o.append(q*w)
if sum(o)==a:
    print('Yes')
elif sum(o)!=a:
    print('No')