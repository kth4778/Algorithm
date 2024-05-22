import sys
import heapq
input = sys.stdin.readline

a=int(input())

for _ in range(a):
    b=int(input())
    que=[]
    grade_list=[]
    count = 1
    for _ in range(b):
        grade=list(map(int,input().split()))
        heapq.heappush(que,grade)
    p=heapq.heappop(que)
    heapq.heappush(grade_list,p[1])

    for _ in range(b-1):
        n=heapq.heappop(que)
        heapq.heappush(grade_list,n[1])
        if grade_list[0]==n[1]:
            count+=1
    print(count)

