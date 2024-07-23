n,k = map(int,input().split())
r = list(map(int,input().split()))
r.append(0)
r.sort()

lst = []
for i in range(1,n+1):
    lst.append(r[i]-r[i-1])

lst.sort(reverse=True)
print(sum(lst[k:]))