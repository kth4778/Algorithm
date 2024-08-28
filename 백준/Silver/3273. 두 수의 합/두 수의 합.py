import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int,input().split())))
x = int(input())
answer = 0

l = 0
r = n - 1

while l < r:
    p = lst[l] + lst[r]
    if p < x:
        l += 1
    elif p > x:
        r -= 1
    else:
        answer += 1
        l += 1

print(answer)
