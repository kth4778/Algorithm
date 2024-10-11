def dfs(visited, move, y, x):
    global answer

    if move > K:
        return

    if y == 0 and x == M - 1 and move == K:
        answer += 1
        return
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and maps[ny][nx] != 'T':
            if [ny,nx] not in visited:
                dfs(visited + [[ny, nx]], move + 1, ny, nx)

N,M,K = map(int,input().split())
maps = [list(input()) for _ in range(N)]
dy = [1,0,0,-1]
dx = [0,1,-1,0]
answer = 0

dfs([[N-1, 0]],1, N - 1, 0)
print(answer)