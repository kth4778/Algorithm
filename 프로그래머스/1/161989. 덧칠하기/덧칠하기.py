def solution(n, m, section):
    visited = [True for _ in range(n)]
    idx = 0
    answer = 0
    
    for s in section:
        visited[s-1] = False
    
    while True:
        if idx == n:
            break
            
        if not visited[idx]:
            answer += 1
            for _ in range(m):
                if idx >= n:
                    break
                
                visited[idx] = True
                idx += 1
        else:
            idx += 1
    
    return answer