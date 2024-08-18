import sys
input = sys.stdin.readline

def bfs(y,x,s,depth):
    global answer
    que = set()
    que.add((y,x,s+maps[y][x],depth))

    while que:
        qy, qx, alpha, new_depth = que.pop()
        answer = max(answer, new_depth)
        
        for i in range(4):
            ny = qy + dy[i]
            nx = qx + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] not in alpha:
                que.add((ny, nx, alpha+maps[ny][nx], new_depth+1))
    return 

n,m = map(int,input().split())
maps = [list(input().strip()) for _ in range(n)]

dx = [1,0,0,-1]
dy = [0,1,-1,0]
answer = 1

bfs(0,0,'',1)
print(answer)