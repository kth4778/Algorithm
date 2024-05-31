from collections import deque

n,k=map(int,input().split())
que=deque([i for i in range(1,n+1)])
result=[]
index=0
while que:
    a=que.popleft()
    index+=1
    if index<k:
        que.append(a)
    else:
        result.append(a)
        index=0
print('<'+str(result)[1:-1]+'>')
