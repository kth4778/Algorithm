from collections import deque

n,k = map(int,input().split())
result = []

visited = [float("inf")] * 100001
que = deque()
que.append([0,n])
visited[n] = 0

while que:
    move,cur = que.popleft()
    if cur == k:
        result.append(move)
    for i in [cur-1, cur+1, cur*2]:
        if 0 <= i <= 100000 and visited[i] >= (move + 1):
            visited[i] = move + 1
            que.append([move+1,i])
a = min(result)
print(a)
print(result.count(a))