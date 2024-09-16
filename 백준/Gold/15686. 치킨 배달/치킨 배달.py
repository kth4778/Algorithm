from itertools import combinations
import sys
input = sys.stdin.readline

def solution(home_lst, chicken_lst):
    answer = 0
    
    for i in home_lst:
        min_size = float("INF")
        for j in chicken_lst:
            min_size = min(min_size, abs(i[0] - j[0]) + abs(i[1] - j[1]))
        answer += min_size
    return answer

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if maps[i][j] != 0:
            if maps[i][j] == 1:
                home.append([i,j])
            else:
                chicken.append([i,j])

answer = float("INF")

for i in combinations(chicken, m):
    answer = min(answer, solution(home, list(i)))

print(answer)