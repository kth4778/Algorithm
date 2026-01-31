import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
x = list(map(int,input().split()))

left = 1
right = N

def is_available(h):
    prev_end = 0

    for lamp in x:
        if lamp - h > prev_end:
            return False
        prev_end = lamp + h
    
    return prev_end >= N

while left <= right:
    middle = (left + right) // 2
    if is_available(middle):
        right = middle - 1
    else:
        left = middle + 1

print(left)