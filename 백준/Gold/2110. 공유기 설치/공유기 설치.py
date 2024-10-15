import sys
input = sys.stdin.readline

def solution(n):
    setNum = lst[0]
    p = C - 1
    index = 1
    while p > 0:
        if index == N:
            return 0
        
        if lst[index] - setNum >= n:
            setNum = lst[index]
            p -= 1
        index += 1
    return 1
    

N,C = map(int,input().split())
lst = sorted([int(input().strip()) for _ in range(N)])

l = 0
r = lst[-1] - lst[0] 

while l <= r:
    mid = (l + r) // 2
    boolean = solution(mid)
    if boolean == 1:
        l = mid + 1
    else:
        r = mid - 1

print(r)