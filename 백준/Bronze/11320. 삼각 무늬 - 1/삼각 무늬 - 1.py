from math import ceil

T = int(input())

def solution(a,b):
    return ceil(a / b) ** 2

for _ in range(T):
    a,b = map(int,input().split())
    print(solution(a,b))