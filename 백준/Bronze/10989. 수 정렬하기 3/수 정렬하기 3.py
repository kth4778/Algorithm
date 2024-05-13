import sys
input = sys.stdin.readline

length=int(input())
result=[0 for _ in range(10001)]
for _ in range(length):
    result[int(input())]+=1
for i in range(10001):
    if result[i]!=0:
        for w in range(result[i]):
            print(i)       
 