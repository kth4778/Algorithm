a,b=map(int,input().split())
p=[]
for i in range(a):
    p.append(0)
for u in range(b):
    z,x,c=map(int,input().split())
    for v in range(z - 1, x):
        p[v] = c
print(*p)