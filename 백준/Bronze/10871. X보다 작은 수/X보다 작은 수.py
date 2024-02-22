a,b=map(int,input().split())
c=list(map(int,input().split()))
if a==len(c):
    for i in c:
        if i<b:
            print(i, end=" ")