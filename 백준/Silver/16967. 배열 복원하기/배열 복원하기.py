H,W,X,Y = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(H + X)]

arrB = [[[] for _ in range(W + Y)] for _ in range(H + X)]
for y in range(H):
    for x in range(W):
        arrB[y][x].append([y, x])
        arrB[y + X][x + Y].append([y,x])

arrA = [[None for _ in range(W)] for _ in range(H)]

for x in range(H + X):
    for y in range(W + Y):
        if len(arrB[x][y]) == 1:
            i,j = arrB[x][y][0]
            arrA[i][j] = maps[x][y]

        elif len(arrB[x][y]) == 2:
            a,b = arrB[x][y][0]
            c,d = arrB[x][y][1]
            if arrA[a][b] != None:
                arrA[c][d] = maps[x][y] - arrA[a][b]
            else:
                arrA[a][b] = maps[x][y] - arrA[c][d]

for i in arrA:
    print(*i)