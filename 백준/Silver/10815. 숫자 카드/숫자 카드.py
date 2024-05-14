import sys
input = sys.stdin.readline


a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))

reti=b+d
result={}

for i in reti:
    if i not in result:
        result[i]=0
    else:
        result[i]=1
for i in d:
    print(result[i],end=' ')