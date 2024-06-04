from collections import deque
que=deque()

n=int(input())
map=[list(input()) for _ in range(n)]
visited=[[False]*n for _ in range(n)]
result=[]

dx=[0,1,-1,0]
dy=[1,0,0,-1]

for i in range(n):
    for w in range(n):
        if map[i][w]=='1' and not visited[i][w]:
            que.append([i,w])
            visited[i][w]=True
            result.append(1)
            while que:
                y,x=que.popleft()
                for p in range(4):
                    nx=dx[p]+x
                    ny=dy[p]+y
                    if 0<=nx<n and 0<=ny<n and map[ny][nx]=='1' and not visited[ny][nx]:
                        que.append([ny,nx])
                        visited[ny][nx]=True
                        result[-1]+=1
result.sort()
print(len(result))
for i in result:
    print(i)