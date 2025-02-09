N,M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]

coordinates = []

for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            coordinates.append([i,j])

y1,x1,y2,x2 = coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1]

print(abs(y1 - y2) + abs(x1 - x2))