a,b=map(int,input().split())
d=list(range(1,a+1))
for o in range(b):
    q,w=map(int,input().split())
    d[q-1],d[w-1]=d[w-1],d[q-1]
print(*d)