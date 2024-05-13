import sys
input = sys.stdin.readline

a=int(input())
N=list(map(int,input().split()))
N1=list(map(int,input().split()))
b=int(input())
b_list=list(map(int,input().split()))
que=[b for a,b in zip(N,N1) if a!=1][::-1]
result=que+b_list
for i in range(b):
    print(result[i],end=' ')
