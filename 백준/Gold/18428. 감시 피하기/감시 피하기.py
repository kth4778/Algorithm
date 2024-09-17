from collections import deque
from itertools import combinations
import copy

def solution(p):
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]

    for y, x in teacher:
        for i in range(4):
            nx = x
            ny = y
            while True:
                nx += dx[i]
                ny += dy[i]
                if not (0 <= nx < n and 0 <= ny < n):
                    break
                if p[ny][nx] == "O":
                    break
                if p[ny][nx] == "S":
                    return False
    return True

n = int(input())
school = [list(input().split()) for _ in range(n)]
empty = []
teacher = []

for y in range(n):
    for x in range(n):
        if school[y][x] == "X":
            empty.append([y,x])
        elif school[y][x]  == "T":
            teacher.append([y,x])

for comb in combinations(empty, 3):
    copy_school = copy.deepcopy(school)
    for y,x in comb:
        copy_school[y][x] = "O"
    if solution(copy_school):
        print("YES")
        exit()

print("NO")
