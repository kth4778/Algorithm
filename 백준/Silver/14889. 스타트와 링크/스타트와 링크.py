from itertools import combinations
import sys
input = sys.stdin.readline

def score(a,b):
    answer = 0
    answer += board[a-1][b-1]
    answer += board[b-1][a-1]
    return answer

def solution(lst):
    a = lst
    b = [i for i in range(1,len(lst) * 2 + 1) if i not in lst]

    a_score = 0
    b_score = 0

    for i in combinations(a,2):
        a_score += score(list(i)[0],list(i)[1])
    
    for i in combinations(b,2):
        b_score += score(list(i)[0],list(i)[1])

    return abs(a_score - b_score)

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

answer = float("INF")
p = [list(j) for j in combinations([i for i in range(1,n+1)], n // 2)]
size = len(p)
p = p[:size//2]


for i in p:
    answer = min(answer, solution(i))
print(answer)