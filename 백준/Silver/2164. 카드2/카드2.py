from collections import deque
que=deque()
a=int(input())
for i in range(1,a+1):
    que.append(i)
while len(que)>=2:
    que.popleft()
    b=que.popleft()
    que.append(b)
print(que[0])