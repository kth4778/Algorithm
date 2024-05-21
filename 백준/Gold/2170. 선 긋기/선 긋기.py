import sys
input = sys.stdin.readline

a=int(input())
b=[list(map(int,input().split())) for _ in range(a)]
b.sort()

length=b[0][1]-b[0][0]
ruler=[b[0][1]]

for i in b[1:]:
    if ruler[0]<=i[1] and ruler[0]>=i[0]:
        length+=i[1]-ruler[0]
        ruler[0]=i[1]
    elif ruler[0]<i[0]:
        length+=i[1]-i[0]
        ruler[0]=i[1]
print(length)