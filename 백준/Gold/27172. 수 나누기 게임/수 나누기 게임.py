import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
Adict = {}
score = [0 for _ in range(N)]

for i in range(N):
    Adict[A[i]] = i

A.sort()

for i in A:
    setNum = i
    index = 2
    c = i * index

    while c <= 1000000:
        if c in Adict:
            score[Adict[setNum]] += 1
            score[Adict[c]] -= 1
        
        index += 1
        c = i * index

print(*score)