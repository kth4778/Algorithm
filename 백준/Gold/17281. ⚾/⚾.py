import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
innings = [list(map(int,input().split())) for _ in range(n)]
answer = 0

number = [i for i in range(1,9)]

for players in permutations(number, 8):
    player = list(players)[:3] + [0] + list(players)[3:]
    score = 0
    number = 0
    for i in range(n):
        out = 0
        p1 = p2 = p3 = 0
            
        while out < 3:
            mode = innings[i][player[number]]

            if mode == 0:
                out += 1
            elif mode == 1:
                score += p3
                p1,p2,p3 = 1,p1,p2
            elif mode == 2:
                score += p2 + p3
                p1,p2,p3 = 0,1,p1
            elif mode == 3:
                score += p1 + p2 + p3
                p1,p2,p3 = 0,0,1
            else:
                score += p1 + p2 + p3 + 1
                p1 = p2 = p3 = 0
            
            number = (number + 1) % 9
    
    answer = max(answer, score)

print(answer)