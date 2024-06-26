from collections import deque

def solution(visited):
    for i in visited:
        for w in i:
            if not w:
                return True
    return False


n,m,k = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(k)]
maps = [['O' for _ in range(m)] for _ in range(n)]

for x1,y1,x2,y2 in paper:
    for i in range(x1,x2):
        for w in range(y1,y2):
            maps[w][i]='#'
maps = maps[::-1]

visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for w in range(m):
        if maps[i][w]=='#':
            visited[i][w]=True

paper_lst = []
dx = [1,0,0,-1]
dy = [0,1,-1,0]

while solution(visited):
    que = deque()
    cnt = 1
    for i in range(n):
        for w in range(m):
            if not visited[i][w]:
                que.append([i,w])
                visited[i][w]=True
                break
        if que:
            break
    while que:
        y,x = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and not visited[ny][nx]:
                cnt+=1
                que.append([ny,nx])
                visited[ny][nx]=True
    paper_lst.append(cnt)
    cnt = 0
print(len(paper_lst))
print(' '.join([str(i) for i in sorted(paper_lst)]))