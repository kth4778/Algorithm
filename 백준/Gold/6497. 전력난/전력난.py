import heapq
import sys
input = sys.stdin.readline

def union(a,b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    
    return parent[x]


while True:
    m,n = map(int,input().split())
    if m == 0 and n == 0:
        break

    parent = [i for i in range(m)]
    que = []
    answer = 0
    sum_nums = 0

    for _ in range(n):
        x,y,z = map(int,input().split())
        heapq.heappush(que, [z,x,y])
        sum_nums += z

    while que:
        cost,a,b = heapq.heappop(que)

        if find(a) != find(b):
            union(a,b)
            answer += cost

    print(sum_nums - answer)