import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(map(int,input().split())))

res = float("INF")
sol_candi = []

for i in range(N - 2):
    cur = lst[i]
    l = i + 1
    r = N - 1

    while l < r:
        cur_sum = cur + lst[l] + lst[r]

        if abs(cur_sum) < res:
            res = abs(cur_sum)
            sol_candi = [lst[i], lst[l], lst[r]]

        if cur_sum > 0:
            r -= 1
        elif cur_sum < 0:
            l += 1
        else:
            print(*sol_candi)
            sys.exit()

print(*sol_candi)