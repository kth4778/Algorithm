def solution(num, index):
    l = 0
    r = N - 1

    while l < r:
        if l == index:
            l += 1
            continue

        if r == index:
            r -= 1
            continue

        p = nums[l] + nums[r]
        
        if p == num:
            return True


        if p > num:
            r -= 1
        else:
            l += 1

N = int(input())
nums = sorted(list(map(int,input().split())))
answer = 0

for i in range(N):
    if solution(nums[i], i):
        answer += 1

print(answer)