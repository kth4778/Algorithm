a=int(input())
b=list(map(int,input().split()))
c=0
for index,i in enumerate(sorted(b)):
    c+=(a-index)*i
print(c)