from collections import deque
n=int(input())

for _ in range(n):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    que={i:c[i] for i in range(a)}
    que2=deque([i for i in range(a)])   
    count=1
    while True:
        if que[que2[0]]==max([que[i] for i in que2]):
            if que2[0]==b:
                print(count)
                break
            else:
                que2.popleft()
                count+=1
        else:
            p=que2.popleft()
            que2.append(p)