import sys
input = sys.stdin.readline

a,b=map(int,input().split())
result1={}
result2={}

for i in range(a):
    p=input().strip()
    result1[p]=i+1
    result2[i+1]=p

for _ in range(b):
    o=input().strip()
    if o.isdigit():
        print(result2[int(o)])
    else:
        print(result1[o])
