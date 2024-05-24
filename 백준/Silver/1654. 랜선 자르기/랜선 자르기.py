import sys
input = sys.stdin.readline

n,k=map(int,input().split())
a=[int(input()) for _ in range(n)]

pl=1
pr=max(a)

while pl<=pr:
    pc=(pl+pr)//2
    st=sum([i//pc for i in a])
    if st>=k:
        pl=pc+1
    else:
        pr=pc-1
print(pr)