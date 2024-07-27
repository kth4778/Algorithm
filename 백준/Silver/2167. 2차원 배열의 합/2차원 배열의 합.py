import sys
input = sys.stdin.readline

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
maps = [[0 for _ in range(m)]] + maps
maps = [[0] + i for i in maps]

newMaps = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        newMaps[i][j] = newMaps[i][j-1] + maps[i][j] + newMaps[i-1][j] - newMaps[i-1][j-1]

t = int(input())
for _ in range(t):
    y1,x1,y2,x2 = map(int,input().split())
    result = newMaps[y2][x2] - newMaps[y2][x1-1] - newMaps[y1-1][x2] + newMaps[y1-1][x1-1]
    print(result)