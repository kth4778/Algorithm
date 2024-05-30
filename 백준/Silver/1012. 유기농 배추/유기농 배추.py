import sys
input = sys.stdin.readline

from collections import deque
a=int(input())
dx=[1,0,0,-1]
dy=[0,1,-1,0]
for _ in range(a):
    q,w,e=map(int,input().split())
    land_dict={tuple(map(int,input().split())):True for _ in range(e)}
    count=0
    que=deque()
    while any(land_dict.values()):
        for i in land_dict:
            if land_dict[i]:
                que.append(i)
                break
        while que:
            x,y=que.popleft()
            land_dict[(x,y)]=False
            for g in range(4):
                nx=x+dx[g]
                ny=y+dy[g]
                if 0<=nx<q and 0<=ny<w and (nx,ny) in land_dict and land_dict[(nx,ny)]:
                    land_dict[(nx,ny)]=False
                    que.append((nx,ny))
        count+=1
    print(count)