from collections import deque

n,k = map(int,input().split())
distance = {i:-1 for i in range(100001)}
visited = {i:[None,i] for i in range(100001)}
distance[n] = 0

que = deque()
que.append(n)

while que:
    cur = que.popleft()
    if cur == k:
        print(distance[k])
        break
    for i in [cur-1, cur+1, cur*2]:
        if 0 <= i <= 100000 and distance[i] == -1:
            distance[i] = distance[cur] + 1
            visited[i][0] = cur
            que.append(i)
result = [k]
node = k
while True:
    if node == n:
        break
    p = visited[node][0]
    result.append(p)
    node = p
print(*result[::-1])