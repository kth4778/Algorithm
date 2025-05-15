from collections import deque

def solution(start):
    visited = [False for _ in range(N)]
    visited[start] = True

    que = deque()

    for i in range(N):
        if friends[start][i] == "Y":
            que.append([i,1])
            visited[i] = True

    while que:
        node, move = que.popleft()
        if move == 2:
            continue

        for i in range(N):
            if friends[node][i] == "Y" and not visited[i]:
                visited[i] = True
                que.append([i, move + 1])


    return sum([1 for i in visited if i]) - 1

N = int(input())
friends = [input() for _ in range(N)]
answer = 0

for i in range(N):
    answer = max(answer, solution(i))

print(answer)