import sys
input = sys.stdin.readline

import heapq
que=[]
a=int(input())
for _ in range(a):
    b=int(input())
    if b!=0:
        heapq.heappush(que,(abs(b),b))
    elif que and b==0:
        print(heapq.heappop(que)[1])
    else:
        print(0)