from itertools import permutations
import copy
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
calculations = [list(map(int,input().split())) for _ in range(K)]
answer = float("INF")
a = [i for i in range(K)]
dy = [0,1,0,-1] #우하좌상
dx = [1,0,-1,0]

for calculation in permutations(calculations, K):
    copy_a = copy.deepcopy(arr)
    for r,c,s in calculation:
        r -= 1
        c -= 1

        for n in range(s, 0, -1):
            tmp = copy_a[r-n][c+n]
            copy_a[r-n][c-n+1:c+n+1] = copy_a[r-n][c-n:c+n]  # ->
            for row in range(r-n, r+n):  # ↑
                copy_a[row][c-n] = copy_a[row+1][c-n]
            copy_a[r+n][c-n:c+n] = copy_a[r+n][c-n+1:c+n+1]  # <-
            for row in range(r+n, r-n, -1):  # ↓
                copy_a[row][c+n] = copy_a[row-1][c+n]
            copy_a[r-n+1][c+n] = tmp

    
    for i in copy_a:
        answer = min(answer, sum(i))

print(answer)