from collections import deque
que=deque()

a=int(input())
b=list(map(int,input().split()))
for i in range(a):
    que.append([i+1,b[i]])
result=[]
while que:
    num,move=que.popleft()
    result.append(str(num))
    if move>0:
        que.rotate(-move+1)
    else:
        que.rotate(-move)
print(' '.join(result))