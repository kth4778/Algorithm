from itertools import combinations
from collections import defaultdict
import copy

def solution(achars, copy_castle, copy_enemy):
    count = 0 

    for y,x in achars:
        copy_castle[y][x] = 8
    
    while True:
        new_enemy = defaultdict(bool)
        change_enemy = []

        for i in copy_enemy:
            new_enemy[tuple(i)] = True

        for y,x in achars:
            q = sorted([(i,j) for i,j in new_enemy if abs(y - i) + abs(x - j) <= D], key = lambda p : ((abs(p[0] - y) + abs(p[1] - x)), p[1] - x))
            if q:
                new_enemy[q[0]] = False

        for key, value in new_enemy.items():
            y,x = key[0], key[1]
            copy_castle[y][x] = 0
            
            if not value:
                count += 1
            else:
                if y + 1 < N:
                    change_enemy.append([y + 1, x])

        if not change_enemy:
            return count
        
        copy_enemy = change_enemy

        for y,x in change_enemy:
            copy_castle[y][x] = 1


N,M,D = map(int,input().split())
castle = []     #성 
enemy = []      #적 좌푯값
answer = 0      #출력값
achar_coordinates = []

for i in range(N):
    lst = list(map(int,input().split()))
    for j in range(M):
        if lst[j] == 1:
            enemy.append([i,j])
    castle.append(lst)

castle.append([9 for _ in range(M)])

for i in range(M):
    achar_coordinates.append([N,i])

for achars in combinations(achar_coordinates, 3):    
    answer = max(answer, solution(achars, copy.deepcopy(castle), copy.deepcopy(enemy)))


print(answer)