def dfs(i,j,score):
    global answer
    
    if j >= M:
        i += 1
        j = 0
        if i >= N:
            answer = max(score, answer)
            return

    if not visited[i][j]:
        for q in range(4):
            ny1, nx1, ny2, nx2 = modeY[q][0] + i, modeX[q][0] + j, modeY[q][1] + i, modeX[q][1] + j
            if 0 <= ny1 < N and 0 <= nx1 < M and 0 <= ny2 < N and 0 <= nx2 < M:
                if not visited[ny1][nx1] and not visited[ny2][nx2]:
                    visited[i][j] = True
                    visited[ny1][nx1] = True
                    visited[ny2][nx2] = True
                    dfs(i, j + 1, score + trees[i][j] * 2 + trees[ny1][nx1] + trees[ny2][nx2])
                    visited[i][j] = False
                    visited[ny1][nx1] = False
                    visited[ny2][nx2] = False
                            
    dfs(i, j + 1, score)


N,M = map(int,input().split())
trees = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
modeY = [[0,1], [-1,0], [-1,0], [0,1]]
modeX = [[-1,0], [0,-1], [0,1], [1,0]]
answer = 0

dfs(0,0,0)
print(answer)