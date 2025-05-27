import sys
sys.setrecursionlimit(10 ** 5)

def DFS(day, history):
    if day == N:
        return history
    
    for cake in riceCake[day + 1][1:]:
        if day == 0:
            visited[day + 1][cake] = True
            p = DFS(day + 1, history + [cake])
            if p != -1:
                return p
            
        else:
            if history[-1] != cake and not visited[day + 1][cake]:
                visited[day + 1][cake] = True
                pp = DFS(day + 1, history + [cake])
                if pp != -1:
                    return pp
                
    return -1

N = int(input())
riceCake = [[]] + [list(map(int,input().split())) for _ in range(N)]
visited = [[False for _ in range(10)] for _ in range(N + 1)]

result = DFS(0,[])
if result == -1:
    print(-1)
else:
    for i in result:
        print(i)