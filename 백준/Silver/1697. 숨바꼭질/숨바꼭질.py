from collections import deque
a,b=map(int,input().split())
que=deque([a])
visited=[-1]*100001
visited[a]=0

while que:
    current=que.popleft()
    if current==b:
        print(visited[current])
        break
    for future in (current-1,current+1,current*2):
        if  0<=future<100001 and visited[future]==-1:
            que.append(future)
            visited[future]=visited[current]+1