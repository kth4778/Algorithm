import sys
import heapq
input = sys.stdin.readline

left_queue = []
right_queue = []

n = int(input())
a = int(input())
print(a)
middle_num = a

for _ in range(n-1):
    num = int(input())
    if num > middle_num:
        heapq.heappush(right_queue,num)
        if len(right_queue) - len(left_queue) >= 2:
            a = heapq.heappop(right_queue)
            heapq.heappush(left_queue,-middle_num)
            middle_num = a
    else:
        heapq.heappush(left_queue,-num)
        if len(left_queue) - len(right_queue) >= 1:
            a = heapq.heappop(left_queue)
            heapq.heappush(right_queue,middle_num)
            middle_num = -a
    print(middle_num)