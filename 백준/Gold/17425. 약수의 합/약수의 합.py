import sys
input = sys.stdin.readline

a=int(input())
b=[int(input()) for _ in range(a)]
max=max(b)

front_devision=[1]*(max+1)
rear_devision=[0]*(max+1)
rear_devision[1]=1

for i in range(2,max+1):
    for w in range(1,max//i+1):
        front_devision[i*w]+=i
    rear_devision[i]=front_devision[i]+rear_devision[i-1]

for i in b:
    print(rear_devision[i])