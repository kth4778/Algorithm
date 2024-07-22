from collections import deque
n,m,k = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
max_num = -float("INF")
dx = [1,0,0,-1]
dy = [0,1,-1,0]

def dfs(y,x,cnt,num):

    if cnt == k:
        global max_num
        max_num = max(max_num,num)
        return
    
    for i in range(y,n):
        for j in range(x if i == y else 0,m):
            if not visited[i][j]:
                switch = True
                for w in range(4):
                    nx = j + dx[w]
                    ny = i + dy[w]
                    if 0 <= nx < m and 0 <= ny < n and visited[ny][nx]:
                        switch = False
                        break
                if switch:
                    visited[i][j] = True
                    dfs(i,j,cnt+1,num+maps[i][j])
                    visited[i][j] = False

dfs(0,0,0,0)
print(max_num)