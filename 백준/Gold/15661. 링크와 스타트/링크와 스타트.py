import sys
from itertools import combinations
input = sys.stdin.readline

answer = float("INF")

def solution(lst):
    scoreA = 0
    scoreB = 0
    for j in combinations(lst,2):
        j = list(j)
        scoreA += s[j[0] - 1][j[1] - 1]
        scoreA += s[j[1] - 1][j[0] - 1]
    

    for i in combinations([j for j in range(1,n+1) if j not in lst], 2):
        i = list(i)
        scoreB += s[i[0] - 1][i[1] - 1]
        scoreB += s[i[1] - 1][i[0] - 1]

    return abs(scoreA - scoreB)
        

n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n//2 + 1):
    for j in combinations([p for p in range(1, n+1)], i):
        p = solution(list(j))
        if p == 0:
            print(0)
            exit()
        else:
            answer = min(answer, solution(list(j)))

print(answer)