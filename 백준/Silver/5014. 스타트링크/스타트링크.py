from collections import deque
f,s,g,u,d=map(int,input().split())

que=deque()
que.append([s,0])
building=[False for _ in range(f+1)]
low_layer=1000000000000

while que:
    layer,cost=que.popleft()
    if layer==g:
        low_layer=min(low_layer,cost)
    building[layer]=True
    if 0<layer+u<=f and not building[layer+u]:
        que.append([layer+u,cost+1])
        building[layer+u]=True
    if 0<layer-d<=f and not building[layer-d]:
        que.append([layer-d,cost+1])
        building[layer-d]=True
if low_layer==1000000000000:
    print('use the stairs')
else:
    print(low_layer)
