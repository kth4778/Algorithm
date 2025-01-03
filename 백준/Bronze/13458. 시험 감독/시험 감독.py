from math import ceil

N = int(input())
M = list(map(int,input().split()))
B,C = map(int,input().split())

answer = 0

for i in M:
    answer += 1
    if i - B > 0:
        answer += ceil((i - B) / C)

print(answer)