from collections import deque
n,m=map(int,input().split())
maps=[list(input()) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
dx=[1,0,0,-1]
dy=[0,1,-1,0]
count=0
start_coordinate=[]
for i in range(n):
    for w in range(m):
        if maps[i][w]=='I':
            start_coordinate.append(i)
            start_coordinate.append(w)
que=deque()
que.append(start_coordinate)
visited[start_coordinate[0]][start_coordinate[1]]=True

while que:
    y,x=que.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and maps[ny][nx]!='X':
            que.append([ny,nx])
            visited[ny][nx]=True
            if maps[ny][nx]=='P':
                count+=1
if count==0:
    print('TT')
else:
    print(count)