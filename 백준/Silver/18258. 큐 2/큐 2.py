import sys
from collections import deque
input = sys.stdin.readline
que=deque()
length=int(input())
for _ in range(length):
    a=input().split()
    if a[0]=='push':
        que.append(int(a[1]))
    elif a[0]=='pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif a[0]=='size':
        print(len(que))
    elif a[0]=='empty':
        if que:
            print(0)
        else:
            print(1)
    elif a[0]=='front':
        if que:
            print(que[0])
        else:
            print(-1)
    else:
        if len(que) != 0:
            print(que[-1])
        else:
            print(-1)