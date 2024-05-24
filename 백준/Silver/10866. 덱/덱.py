from collections import deque
import sys
input = sys.stdin.readline

que=deque()
a=int(input())
for _ in range(a):
    de=input().strip().split()
    if de[0]=='push_front':
        que.appendleft(int(de[1]))
    elif de[0]=='push_back':
        que.append(int(de[1]))
    elif de[0]=='pop_front':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif de[0]=='pop_back':
        if que:
            print(que.pop())
        else:
            print(-1)
    elif de[0]=='size':
        print(len(que))
    elif de[0]=='empty':
        print(int(not que))
    elif de[0]=='front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif de[0]=='back':
        if que:
            print(que[-1])
        else:
            print(-1)
    