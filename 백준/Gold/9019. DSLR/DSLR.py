from collections import deque

def regi(num,s):
    if s == 'D':
        return (2*num) % 10000
    elif s == 'S':
        if num == 0:
            return 9999
        return num-1
    elif s == 'L':
        num = str(num).zfill(4)
        return int(num[1:]+num[:1])
    elif s == 'R':
        num = str(num).zfill(4)
        return int(num[-1:]+num[:-1])


t = int(input())
for _ in range(t):
    A,B = map(int,input().split())
    que = deque()
    visited = set([A])
    dslr = ['D','S','L','R']
    que.append([A,''])

    while True:
        m,s = que.popleft()
        if m == B:
            print(s)
            break
        for i in range(4):
            next_num = regi(m,dslr[i])
            if next_num not in visited:
                que.append([next_num,s+dslr[i]])
                visited.add(next_num)