n = int(input())
lst = list(map(int,input().split()))
lst.sort()

l = 0
r = n - 1

set_num = abs(lst[l] + lst[r])
answer = [lst[l], lst[r]]

while l < r:
    left = lst[l]
    right = lst[r]

    sum = left + right

    if abs(sum) < set_num:
        set_num = abs(sum)
        answer = [left, right]
        if set_num == 0:
            break
    if sum < 0:
        l += 1
    else:
        r -= 1

print(answer[0], answer[1])