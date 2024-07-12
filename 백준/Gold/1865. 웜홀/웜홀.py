import sys
input = sys.stdin.readline

def bf():
    for i in range(n):
        for j in range(len(graph)):
            cur, next_node, cost = graph[j]
            if distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                if i == n-1:
                    return True
    return False


t = int(input())
for _ in range(t):
    n,m,w = map(int,input().split())
    graph = []
    distance = {i:1e9 for i in range(1,n+1)}
    
    for _ in range(m):
        a,b,cost = map(int,input().split())
        graph.append([a,b,cost])
        graph.append([b,a,cost])
    for _ in range(w):
        a,b,cost = map(int,input().split())
        graph.append([a,b,-cost])

    if bf():
        print("YES")
    else:
        print("NO")