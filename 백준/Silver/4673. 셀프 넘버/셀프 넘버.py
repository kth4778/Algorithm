from collections import deque


visited = [False for _ in range(10001)]
que = deque()

que.append(1)

while que:
    num = que.popleft()
    if num < 10000:
        if not visited[num + 1]:
            que.append(num + 1)
        n = num

    for i in str(num):
        n += int(i)

    if 0 <= n < 10001:
        if not visited[n]:
            visited[n] = True
            que.append(n)

for i in range(1, 10001):
    if not visited[i]:
        print(i)