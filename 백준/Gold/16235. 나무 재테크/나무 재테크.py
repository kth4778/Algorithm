#봄: 자신의 나이만큼 양분 먹고, 나이 +1, 나이가 어린 나무부터, 못먹으면 사망
#여름: 봄에 죽은 나무가 양분으로 변함 나누기 2
#가을: 나무의 나이가 5의 배수이면 근방 9개 구역에 나이가 1인 나무 생성
#겨울: S2D2가 땅을 돌아다니며 양분 추가

from collections import deque

n,m,k = map(int,input().split())
food = [list(map(int,input().split())) for _ in range(n)]
land = [[5 for _ in range(n)] for _ in range(n)]
trees = []
dy = [1,1,1,0,0,-1,-1,-1]
dx = [-1,0,1,-1,1,-1,0,1]

for _ in range(m):
    y,x,age = map(int,input().split())
    trees.append([y - 1, x - 1, age])

trees.sort(key = lambda x : x[2])
trees = deque(trees)

def spring():
    new_trees = deque([])
    dead_trees = deque([])

    while trees:
        y,x,age = trees.popleft()
        if age <= land[y][x]:
            land[y][x] -= age
            new_trees.append([y,x,age + 1])
        else:
            dead_trees.append([y,x,age])
    
    while dead_trees:
        y,x,age = dead_trees.popleft()
        land[y][x] += age // 2
    
    return new_trees

def fall():
    global trees
    new_trees = deque()

    for y,x,age in trees:
        if age % 5 == 0:
            for i in range(8):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < n:
                    new_trees.append([ny,nx,1])
    new_trees.extend(trees)
    
    trees = new_trees

    for i in range(n):
        for j in range(n):
            land[i][j] += food[i][j]

for _ in range(k):
    trees = spring()
    fall()

print(len(trees))