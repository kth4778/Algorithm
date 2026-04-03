from collections import deque

def solution(info, edges):
    length = len(info)
    graph = [[] for _ in range(length)]
    answer = 1
    
    for s, e in edges:
        graph[s].append(e)

    que = deque()
    que.append([0, 1, 0, set()])
    
    while que:
        node, s, w, visited = que.popleft()
        
        answer = max(answer, s)
        visited.update(graph[node])
        
        for next_node in visited:
            if info[next_node] == 0:
                que.append([next_node, s + 1, w, visited - {next_node}])
            else:
                if s > w + 1:
                    que.append([next_node, s, w + 1, visited - {next_node}])
    
    return answer