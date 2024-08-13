from itertools import permutations

def kits(lst):
    p = 0
    for i in lst:
        p += (-k + i)
        if p < 0:
            return False
    return True

n,k = map(int,input().split())
nums = list(map(int,input().split()))
answer = 0

for i in permutations(nums,n):
    if kits(list(i)):
        answer += 1

print(answer)