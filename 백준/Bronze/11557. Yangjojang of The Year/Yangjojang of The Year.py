import heapq

T = int(input())

for _ in range(T):
    N = int(input())
    que = []

    for _ in range(N):
        a,b = input().split()
        heapq.heappush(que,[-int(b), a])
    
    size, name = heapq.heappop(que)
    print(name)