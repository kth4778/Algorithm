n,l=map(int,input().split())
m={i:True for i in sorted(list(map(int,input().split())))}
count=0
for p in m:
    if m[p]:
        for w in range(p,p+l):
            if w in m:
                m[w]=False
        count+=1
print(count)