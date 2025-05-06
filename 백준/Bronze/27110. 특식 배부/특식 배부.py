score = 0

N = int(input())
p = list(map(int,input().split()))

for i in range(3):
    score += min(N,p[i])

print(score)