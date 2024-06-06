from math import ceil
a=int(input())
tshirt=list(map(int,input().split()))
t,p=map(int,input().split())
count=0
for i in tshirt:
    count+=ceil(i/t)
print(count)
print(a//p,a%p)
