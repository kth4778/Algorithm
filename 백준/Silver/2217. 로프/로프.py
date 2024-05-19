import sys
input = sys.stdin.readline

a=int(input())
b=sorted([int(input()) for _ in range(a)],reverse=True)
result=[]
count=1
for i in b:
    result.append(i*count)
    count+=1
print(max(result))