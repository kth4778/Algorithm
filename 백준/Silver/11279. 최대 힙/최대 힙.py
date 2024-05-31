import sys
input = sys.stdin.readline

import heapq
que=[]
n=int(input())
for _ in range(n):
    x=int(input())
    if x==0:
        if que:
            print(-heapq.heappop(que))
        else:
            print(0)
    else:
        heapq.heappush(que,-x)
