from collections import deque
import sys
input = sys.stdin.readline

que=deque()
a=int(input())

for _ in range(a):
    b=input().split()
    if b[0]=='push':
        que.append(int(b[1]))
    elif b[0]=='pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif b[0]=='size':
        print(len(que))
    elif b[0]=='empty':
        print(int(not que))
    elif b[0]=='front':
        if que:
            print(que[0])
        else:
            print(-1)
    else:
        if que:
            print(que[-1])
        else:
            print(-1)