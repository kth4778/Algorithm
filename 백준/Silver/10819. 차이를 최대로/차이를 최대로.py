from itertools import permutations

def solution(lst):
    answer = 0
    for i in range(1, n):
        answer += abs(l[lst[i]] - l[lst[i - 1]])
    return answer

n = int(input())
l = list(map(int,input().split()))

answer = 0

for i in permutations([j for j in range(n)], n):
    answer = max(answer, solution(list(i)))

print(answer)