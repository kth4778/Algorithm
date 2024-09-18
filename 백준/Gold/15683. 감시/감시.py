import copy 

N, M = map(int,input().split())
office, cctv = [], []

modes = [[], 
         [[0], [1], [2], [3]], 
         [[0, 2], [1, 3]],
         [[0, 1], [1, 2], [2, 3], [0, 3]],
         [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], 
         [[0, 1, 2, 3]]]
# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


for i in range(N):
    p = list(map(int,input().split()))
    office.append(p)
    for j in range(M):
        if p[j] in [1,2,3,4,5]:
            cctv.append([p[j],i,j])
        
def fill(y,x,maps,mode):
    for m in mode:
        ny = y
        nx = x

        while True:
            ny += dy[m]
            nx += dx[m]
            if not (0 <= ny < N and 0 <= nx < M):
                break
            if maps[ny][nx] == 6:
                break
            if maps[ny][nx] == 0:
                maps[ny][nx] = -1

def dfs(depth, maps):
    global ans
    if depth == len(cctv):
        cnt = 0
        for i in range(N):
            cnt += maps[i].count(0)
        ans = min(ans, cnt)
        return
    
    temp = copy.deepcopy(maps)
    cctv_mode, y, x = cctv[depth]
    for mode in modes[cctv_mode]:
        fill(y,x,temp,mode)
        dfs(depth + 1, temp)
        temp = copy.deepcopy(maps)


ans = float("INF")
dfs(0, office)
print(ans)