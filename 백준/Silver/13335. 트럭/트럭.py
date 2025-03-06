from collections import deque

N,W,L = map(int,input().split())
p = deque(list(map(int,input().split())))
time = 0
weight = 0
length = 0
que = deque()

while que or p:
    # print(f"time: {time}, weight: {weight}, length: {length}, que: {que}, p: {p}")
    for _ in range(len(que)):
        w, t = que.popleft()
        if t < W:
            que.append([w, t + 1])
        else:
            weight -= w
            length -= 1

    if p:
        w = p[0]
        if w + weight <= L and length + 1 <= W:
            que.append([p.popleft(),1])
            weight += w
            length += 1

    time += 1

print(time)