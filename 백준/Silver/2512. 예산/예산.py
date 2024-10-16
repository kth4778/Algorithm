import sys
input = sys.stdin.readline

def solution(n):
    p = budget
    for num in nums:
        if num <= n:
            p -= num
        else:
            p -= n
        if p < 0:
            return False
    return True


N = int(input().strip())
nums = sorted(list(map(int,input().split())))
budget = int(input().strip())

l = 0
r = nums[-1]

while l <= r:
    mid = (l + r) // 2
    if solution(mid):
        l = mid + 1
    else:
        r = mid - 1

print(r)