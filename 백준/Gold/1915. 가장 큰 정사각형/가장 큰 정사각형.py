import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

answer = 0

for y in range(n):
    for x in range(m):
        if y == 0 or x == 0:
            dp[y][x] = int(board[y][x])
    
        elif board[y][x] == "0":
            dp[y][x] = 0

        else:
            dp[y][x] = min(dp[y - 1][x], dp[y - 1][x - 1], dp[y][x - 1]) + 1

        answer = max(answer, dp[y][x])

print(answer ** 2)