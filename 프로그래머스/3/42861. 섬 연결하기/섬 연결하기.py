import heapq

def solution(n, costs):
    def union(a, b):
        node_a = find(a)
        node_b = find(b)
        
        if node_a > node_b:
            graph[node_a] = node_b        
        else:
            graph[node_b] = node_a
    
    def find(x):
        if graph[x] != x:
            graph[x] = find(graph[x])
        
        return graph[x]
    
    que = []
    graph = [i for i in range(n + 1)]
    answer = 0
    
    for a, b, cost in costs:
        heapq.heappush(que, [cost, a, b])
    
    while que:
        cost, a, b = heapq.heappop(que)
        
        if find(a) != find(b):
            answer += cost
            union(a, b)
    
    return answer