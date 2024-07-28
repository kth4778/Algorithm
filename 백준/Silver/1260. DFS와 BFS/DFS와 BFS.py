from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())
maps = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    maps[a].append(b)
    maps[b].append(a)
maps = [sorted(i) for i in maps]

bfs_visited = {i:False for i in range(1,n+1)}
dfs_visited = {i:False for i in range(1,n+1)}
dfs_lst = []
bfs_lst = []

def dfs(start):
    if not dfs_visited[start]:
        dfs_visited[start] = True
        dfs_lst.append(str(start))
    for i in maps[start]:
        if not dfs_visited[i]:
            dfs(i)
    

def bfs(start):
    que = deque()
    que.append(start)
    bfs_visited[start] = True
    bfs_lst.append(str(start))

    while que:
        cur = que.popleft()

        for i in maps[cur]:
            if not bfs_visited[i]:
                que.append(i)
                bfs_lst.append(str(i))
                bfs_visited[i] = True

bfs(v)
dfs(v)
print(' '.join(dfs_lst))
print(' '.join(bfs_lst))