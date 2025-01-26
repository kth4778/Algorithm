import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p,m = map(int,input().split())
    chair = {i:0 for i in range(1, m + 1)}
    answer = 0

    for _ in range(p):
        i = int(input().strip())
        chair[i] += 1
    
    for i in chair:
        if chair[i] > 1:
            answer += chair[i] - 1

    print(answer)
