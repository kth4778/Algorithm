a,b=map(int,input().split())
set1=[]

count=0
for _ in range(a):
    set1.append(input())
for _ in range(b):
    p=input()
    if p in set1:
        count+=1
print(count)