from collections import deque
import sys
input = sys.stdin.readline

def move(mode,y,x):
    while True:
        y += dy[mode]
        x += dx[mode]

        if 0 > y or 0 > x or y >= N or x >= M:
            break
        elif maps[y][x] == "#":
            break
        elif maps[y][x] == "O":
            return True
    y -= dy[mode]
    x -= dx[mode]
    return y,x

def left(by,bx,ry,rx):
    if bx < rx:
        blue = move(0, by, bx)
        
        if blue == True:
            return False
        maps[blue[0]][blue[1]] = "#"
        red = move(0, ry, rx)
        maps[blue[0]][blue[1]] = "."

        if red == True:
            return True

    else:
        red = move(0, ry, rx)
        
        if red == True:
            p = move(0, by, bx)
            if p == True:
                return False
            else:
                return True

        maps[red[0]][red[1]] = "#"
        blue = move(0, by, bx)
        maps[red[0]][red[1]] = "."

        if blue == True:
            return False

    return [blue[0], blue[1], red[0], red[1]]

def right(by,bx,ry,rx):
    if bx > rx:
        blue = move(1, by, bx)
        
        if blue == True:
            return False
        maps[blue[0]][blue[1]] = "#"
        red = move(1, ry, rx)
        maps[blue[0]][blue[1]] = "."

        if red == True:
            return True

    else:
        red = move(1, ry, rx)
        
        if red == True:
            p = move(1, by, bx)
            if p == True:
                return False
            else:
                return True

        maps[red[0]][red[1]] = "#"
        blue = move(1, by, bx)
        maps[red[0]][red[1]] = "."

        if blue == True:
            return False

    return [blue[0], blue[1], red[0], red[1]]

def up(by,bx,ry,rx):
    if by < ry:
        blue = move(2, by, bx)
        
        if blue == True:
            return False
        maps[blue[0]][blue[1]] = "#"
        red = move(2, ry, rx)
        maps[blue[0]][blue[1]] = "."

        if red == True:
            return True

    else:
        red = move(2, ry, rx)
        
        if red == True:
            p = move(2, by, bx)
            if p == True:
                return False
            else:
                return True

        maps[red[0]][red[1]] = "#"
        blue = move(2, by, bx)
        maps[red[0]][red[1]] = "."

        if blue == True:
            return False

    return [blue[0], blue[1], red[0], red[1]]

def down(by,bx,ry,rx):
    if by > ry:
        blue = move(3, by, bx)
        
        if blue == True:
            return False
        maps[blue[0]][blue[1]] = "#"
        red = move(3, ry, rx)
        maps[blue[0]][blue[1]] = "."

        if red == True:
            return True

    else:
        red = move(3, ry, rx)
        
        if red == True:
            p = move(3, by, bx)
            if p == True:
                return False
            else:
                return True

        maps[red[0]][red[1]] = "#"
        blue = move(3, by, bx)
        maps[red[0]][red[1]] = "."

        if blue == True:
            return False

    return [blue[0], blue[1], red[0], red[1]]

N,M = map(int,input().split())
maps = []

dy, dx = [0,0,-1,1], [-1,1,0,0]
visited = []

redCoordinate = None, None
blueCoordinate = None, None
holeCoordinate = None, None

for y in range(N):
    p = list(input().strip())
    maps.append(p)
    for x in range(M):
        if p[x] == "R":
            redCoordinate = y,x
            p[x] = "."
        
        elif p[x] == "B":
            blueCoordinate = y,x
            p[x] = "."

que = deque()
que.append([blueCoordinate[0], blueCoordinate[1], redCoordinate[0], redCoordinate[1], 0])

while que:
    by,bx,ry,rx,moves = que.popleft()
    if moves == 10:
        continue

    l = left(by,bx,ry,rx)
    r = right(by,bx,ry,rx)
    u = up(by,bx,ry,rx)
    d = down(by,bx,ry,rx)

    if l == True:
        print(moves + 1)
        sys.exit()
    elif l != False and [l[0], l[1], l[2], l[3]] not in visited:
        que.append([l[0], l[1], l[2], l[3], moves + 1])
        visited.append([l[0], l[1], l[2], l[3]])

    if r == True:
        print(moves + 1)
        sys.exit()
    elif r != False and [r[0], r[1], r[2], r[3]] not in visited:
        que.append([r[0], r[1], r[2], r[3], moves + 1])
        visited.append([r[0], r[1], r[2], r[3]])

    if u == True:
        print(moves + 1)
        sys.exit()
    elif u != False and [u[0], u[1], u[2], u[3]] not in visited:
        que.append([u[0], u[1], u[2], u[3], moves + 1])
        visited.append([u[0], u[1], u[2], u[3]])        

    if d == True:
        print(moves + 1)
        sys.exit()
    elif d != False and [d[0], d[1], d[2], d[3]] not in visited:
        que.append([d[0], d[1], d[2], d[3], moves + 1])
        visited.append([d[0], d[1], d[2], d[3]])
print(-1)