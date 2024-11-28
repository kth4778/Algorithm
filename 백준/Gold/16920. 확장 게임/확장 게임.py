from collections import deque
import sys
input = sys.stdin.readline

def solution(coordinates, info):
    next_coordinates = []

    que = deque()
    for y, x in coordinates:
        que.append([y,x,0])

    while que:
        y,x,count = que.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if boards[ny][nx] == '.':
                    if count <  S[info]:
                        next_coordinates.append([ny,nx])
                        que.append([ny,nx,count + 1])
                        answer[info] += 1
                        boards[ny][nx] = str(info)

    return next_coordinates


N,M,P = map(int,input().split())
players = [[] for _ in range(P + 1)]
S = [None] + list(map(int,input().split()))
boards = []
dy = [-1,0,0,1]
dx = [0,-1,1,0]
answer = [0 for _ in range(P + 1)]

for i in range(N):
    board = list(input().strip())
    boards.append(board)
    for j in range(M):
        if board[j] != '.' and board[j] != '#':
            players[int(board[j])].append([i,j])
            answer[int(board[j])] += 1

while True:
    for i in range(1, P + 1):
        players[i] = solution(players[i],i)

    switch = False

    for i in players:
        if i:
            switch = True
            break
    
    if not switch:
        break

print(*answer[1:])