N = int(input())

dp = [[0 for _ in range(N)] for _ in range(N)]
maps = [list(map(int,input().split())) for _ in range(N)]
dx = [1,0]
dy = [0,1]

answer = 0
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j] > 0:
            p = maps[i][j]
            nx1, ny1 = j + dx[0] * p, i + dy[0] * p
            nx2, ny2 = j + dx[1] * p, i + dy[1] * p

            if 0 <= ny1 < N and 0 <= nx1 < N:
                if ny1 == N - 1 and nx1 == N - 1:
                    answer += dp[i][j]
                else:
                    dp[ny1][nx1] += dp[i][j]
            
            if 0 <= ny2 < N and 0 <= nx2 < N:
                if ny2 == N - 1 and nx2 == N - 1:
                    answer += dp[i][j]
                else:    
                    dp[ny2][nx2] += dp[i][j]

print(answer)