from collections import deque

def solution(visited):
    for i in visited:
        for w in i:
            if not w:
                return True
    return False

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
painting_lst = []
dx = [1,0,0,-1]
dy = [0,1,-1,0]

que_set = set()
for i in range(n):
    for w in range(m):
        if maps[i][w]==1:
            que_set.add((i,w))

while que_set:
    que = deque()
    a,b = que_set.pop()
    visited[a][b]=True
    que.append([a,b])
    cnt = 1
    while que:
        y,x = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and maps[ny][nx]==1 and not visited[ny][nx]:
                que.append([ny,nx])
                visited[ny][nx]=True
                que_set.remove((ny,nx))
                cnt += 1
    painting_lst.append(cnt)
print(len(painting_lst))
if not painting_lst:
    print(0)
else:
    print(max(painting_lst))