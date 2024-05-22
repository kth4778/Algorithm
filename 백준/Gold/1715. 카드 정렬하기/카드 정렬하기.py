import sys
import heapq
input = sys.stdin.readline

result=[]
count=0
a=int(input())
for _ in range(a):
    b=int(input())
    heapq.heappush(result,b)
while len(result)>1:
    q=heapq.heappop(result)
    w=heapq.heappop(result)
    count+=q+w
    heapq.heappush(result,q+w)
print(count)