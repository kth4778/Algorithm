from collections import deque

n=int(input())
maps=[list(input()) for _ in range(n)]
maps1=[[]*n for _ in range(n)]
visited=[[False]*n for _ in range(n)]
visited1=[[False]*n for _ in range(n)]
dx=[1,0,0,-1]
dy=[0,1,-1,0]

for i in range(n):
    for w in range(n):
        if maps[i][w]=='R':
            maps1[i].append('G')
        else:
            maps1[i].append(maps[i][w])

def general():
    que=deque()
    count=0
    while True:
        if all([all(i) for i in visited]):
            break
        switch=True
        for i in range(n):
            for w in range(n):
                if not visited[i][w]:
                    que.append([i,w,maps[i][w]])
                    visited[i][w]=True
                    switch=False
                    break
            if not switch:
                break
        count+=1
        while que:
            y,x,color=que.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<n and not visited[ny][nx] and maps[ny][nx]==color:
                    que.append([ny,nx,color])
                    visited[ny][nx]=True
    return count
def patiant():
    que=deque()
    count=0
    while True:
        if all([all(i) for i in visited1]):
            break
        switch=True
        for i in range(n):
            for w in range(n):
                if not visited1[i][w]:
                    que.append([i,w,maps1[i][w]])
                    visited1[i][w]=True
                    switch=False
                    break
            if not switch:
                break
        count+=1
        while que:
            y,x,color=que.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<n and not visited1[ny][nx] and maps1[ny][nx]==color:
                    que.append([ny,nx,color])
                    visited1[ny][nx]=True
    return count
print(general(),end=' ')
print(patiant())