from collections import deque
M,N=map(int,input().split())
tomato=[]
for i in range(N):
    tomato.append(list(map(int,input().split())))

day_count=0
que=deque()
for i in range(N):
    for w in range(M):
        if tomato[i][w]==1:
            que.append([i,w])
    dx=[1,0,0,-1]
    dy=[0,1,-1,0]
while que:
    day_count+=1
    for _ in range(len(que)):
        y,x=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<M and 0<=ny<N and tomato[ny][nx]==0:
                tomato[ny][nx]=1
                que.append([ny,nx])
day_count-=1
if len([1 for i in tomato for w in i if w==0])!=0:
    day_count=-1
print(day_count)
