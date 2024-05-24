import sys
from collections import deque

input = sys.stdin.readline

a=int(input())
b=list(int(input()) for _ in range(a))

que=b[::-1]
sequnce=[i for i in range(a,0,-1)]
lst=[]
trash=[]
result=deque()
while True:
    if not trash:
        trash.append(sequnce.pop())
        result.append('+')
    else:
        if trash[-1]!=que[-1]:
            trash.append(sequnce.pop())
            result.append('+')
        elif trash[-1]==que[-1]:
            lst.append(trash.pop())
            que.pop()
            result.append('-')

    if lst==b :
        for i in range(a*2):
            print(result.popleft())
        break
    elif not sequnce and trash[-1]!=que[-1]:
        print('NO')
        break
