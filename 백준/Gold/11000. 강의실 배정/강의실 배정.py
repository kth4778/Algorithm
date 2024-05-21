import heapq
import sys
input = sys.stdin.readline

a=int(input())
result=[tuple(map(int,input().split())) for _ in range(a)]
result.sort()

que=[]
heapq.heappush(que,result[0][1])

for i in range(1,a):
    if que[0]<=result[i][0]:
        heapq.heappop(que)
    heapq.heappush(que,result[i][1])
print(len(que))