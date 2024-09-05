from collections import deque

n = int(input())
lst = [map(int,input().split()) for _ in range(n)]

max_answer = 0
que = deque()

for index,lst in enumerate(lst):
    t,p = lst
    que.append([0,0])
    for _ in range(len(que)):
        remaining_days, total_cost = que.popleft()
        if remaining_days + index <= n:
            max_answer = max(max_answer, total_cost)
        
        que.append([remaining_days - 1, total_cost])
        if remaining_days < 2:
            que.append([t, total_cost + p])
for i in range(len(que)):
    remaining_days, total_cost = que.popleft()
    if remaining_days + index <= n:
        max_answer = max(max_answer, total_cost)
    
print(max_answer)