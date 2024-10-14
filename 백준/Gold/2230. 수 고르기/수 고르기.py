import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = sorted([int(input().strip()) for _ in range(N)])

l = 0
r = 0
answer = lst[-1] - lst[0]

while r < N and l < N:
    p = lst[r] - lst[l]

    if p < M:
        r += 1
    
    if p >= M:
        answer = min(answer, p)
        l += 1 

print(answer)