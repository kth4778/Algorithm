black={0:1,1:1,2:2,3:2,4:2,5:8}
a=list(map(int,input().split()))
t=[]
for i in range(6):
    t.append(black[i]-a[i])
print(*t)