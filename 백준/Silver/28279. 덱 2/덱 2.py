from collections import deque
import sys
input = sys.stdin.readline
a=int(input())
que=deque()

for i in range(a):
    b=input().split()
    if b[0]=='1':
        que.insert(0,int(b[1]))
    elif b[0]=='2':
        que.append(int(b[1]))
    elif b[0]=='3':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif b[0]=='4':
        if que:
            print(que.pop())
        else:
            print(-1)
    elif b[0]=='5':
        print(len(que))
    elif b[0]=='6':
        print(int(not que))
    elif b[0]=='7':
        if que:
            print(que[0])
        else:
            print(-1)
    elif b[0]=='8':
        if que:
            print(que[-1])
        else:
            print(-1)