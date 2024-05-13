import sys
input = sys.stdin.readline

length=int(input())
result=[]
for _ in range(length):
    result.append(int(input()))
for i in sorted(result):
    print(i)