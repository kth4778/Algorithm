import sys
input = sys.stdin.readline

n,k=map(int,input().split())
result=list(map(int,input().split()))
accrue_sum=[0]
for i in result:
    accrue_sum.append(accrue_sum[-1]+i)
for _ in range(k):
    a,b=map(int,input().split())
    print(accrue_sum[b]-accrue_sum[a-1])