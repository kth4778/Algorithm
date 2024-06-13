import sys
input = sys.stdin.readline
a=int(input())
stairs=[int(input()) for _ in range(a)]
if a==1:
    print(stairs[0])
elif a==2:
    print(sum(stairs))
else:
    stairs_list=[0]*a
    stairs_list[0]=stairs[0]
    stairs_list[1]=stairs[0]+stairs[1]
    stairs_list[2]=max(stairs[0]+stairs[2],stairs[1]+stairs[2])
    for i in range(3,a):
        stairs_list[i]=max(stairs_list[i-2]+stairs[i],stairs_list[i-3]+stairs[i-1]+stairs[i])
    print(stairs_list[-1])