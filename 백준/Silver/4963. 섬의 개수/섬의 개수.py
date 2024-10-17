from collections import deque
import sys
input = sys.stdin.readline

def dfs(m,n):
    answer = 0
    que = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    dx = [1,0,0,-1,-1,1,1,-1]
    dy = [0,1,-1,0,1,1,-1,-1]

    for y in range(n):
        for x in range(m):
            if maps[y][x] == 1 and not visited[y][x]:
                answer += 1
                visited[y][x] = True
                que.append([y,x])
                
                while que:
                    q,w = que.popleft()
                    for i in range(8):
                        ny = q + dy[i]
                        nx = w + dx[i]
                        if 0 <= ny < n and 0 <= nx < m:
                            if maps[ny][nx] == 1 and not visited[ny][nx]:
                                visited[ny][nx] = True
                                que.append([ny, nx])
    return answer

while True:
    M,N = map(int,input().split())
    if N == 0 and M == 0:
        exit()

    maps = [list(map(int,input().split())) for _ in range(N)]
    print(dfs(M,N))