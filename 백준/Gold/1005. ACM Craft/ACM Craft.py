from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

def solution():
    que = deque()

    for i in range(1, N + 1):
        if degree[i] == 0:
            que.append(i)
    
    while que:
        cur = que.popleft()

        if cur == setBuilding:
            return sum(dp[setBuilding])

        for next_node in graph[cur]:
            dp[next_node][0] = max(dp[next_node][0], sum(dp[cur]))
            degree[next_node] -= 1
            
            if degree[next_node] == 0:
                que.append(next_node)

for _ in range(T):
    N,K = map(int,input().split())
    buildTime = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(N + 1)]
    degree = [0 for _ in range(N + 1)]

    for _ in range(K):
        a,b = map(int,input().split())
        graph[a].append(b)
        degree[b] += 1

    setBuilding = int(input())
    dp = [[0, buildTime[i]] for i in range(N + 1)]

    print(solution())

