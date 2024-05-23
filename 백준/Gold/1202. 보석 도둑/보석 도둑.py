import sys
import heapq
input = sys.stdin.readline

n,k=map(int,input().split())
gems=[list(map(int,input().split())) for _ in range(n)]
bags=[int(input().strip()) for _ in range(k)]

bags.sort()
gems.sort()

money=0
que=[]

for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(que,-gems[0][1])
        heapq.heappop(gems)
    if que:
        money-=heapq.heappop(que)
print(money)