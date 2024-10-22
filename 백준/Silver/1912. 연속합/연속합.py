n = int(input())
nums = list(map(int,input().split()))
answer = nums[0]
num = 0

for i in nums:
    num += i
    answer = max(num, answer)
    if num < 0:
        num = 0

print(answer)