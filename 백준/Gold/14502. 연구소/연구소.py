from itertools import combinations
from collections import deque
import copy

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
lst = []
virus = []
for i in range(n):
    for w in range(m):
        if maps[i][w] == 0:
            lst.append([i,w])
        elif maps[i][w] == 2:
            virus.append([i,w])

def solution(lab,lst,virus):
    for y,x in lst:
        lab[y][x] = 1
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    que = deque()

    for i in virus:
        que.append(i)
    
    while que:
        y,x = que.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and lab[ny][nx] == 0:
                que.append([ny,nx])
                lab[ny][nx] = 2
                visited[ny][nx] = True
    
    cnt = 0
    for q in range(n):
        for w in range(m):
            if lab[q][w] == 0:
                cnt += 1
    return cnt

result = 0

for i in list(combinations(lst,3)):
    result = max(solution(copy.deepcopy(maps),i,virus),result)

print(result)