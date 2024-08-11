from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    que = deque()
    que.append(start)
    ans = 1
    time = True

    while que:
        for _ in range(len(que)):
            y,x,w = que.popleft()

            if y == n-1 and x == m -1:
                print(ans)
                return
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 > nx or m <= nx or 0 > ny or n <= ny or visited[ny][nx] <= w:
                    continue

                if maps[ny][nx] == '0':
                    que.append([ny,nx,w])
                    visited[ny][nx] = w
                
                elif w < k:
                    if time:
                        que.append([ny,nx,w+1])
                        visited[ny][nx] = w+1
                    else:
                        que.append([y,x,w])

        time = not time
        ans += 1
    print(-1)
    return

n,m,k = map(int,input().split())
maps = [list(input().strip()) for _ in range(n)]
visited = [[k+1 for _ in range(m)] for _ in range(n)]
result = -1
dy = [1,0,0,-1]
dx = [0,1,-1,0]
visited[0][0] = 0

bfs([0,0,0])