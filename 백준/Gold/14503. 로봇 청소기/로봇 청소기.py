n,m=map(int,input().split())
r,c,d=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]

visited=[[False for _ in range(m)] for _ in range(n)]
dr=[-1,0,1,0]
dc=[0,1,0,-1]
cnt=1
visited[r][c]=True

while True:
    flag=0

    for _ in range(4):
        d=(d+3)%4
        nr=r+dr[d]
        nc=c+dc[d]
        if 0<=nr<n and 0<=nc<m and maps[nr][nc]==0 and not visited[nr][nc]:
            visited[nr][nc]=True
            flag=1
            r=nr
            c=nc
            cnt+=1
            break
    if flag==0:
        if maps[r+dr[(d+2)%4]][c+dc[(d+2)%4]]==1:
            print(cnt)
            break
        else:
            r=r+dr[(d+2)%4]
            c=c+dc[(d+2)%4]