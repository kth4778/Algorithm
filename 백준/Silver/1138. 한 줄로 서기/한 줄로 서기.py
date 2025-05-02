from itertools import permutations

def countHigh(lst, n):
    count = 0
    index = 0

    while lst[index] != n:
        if lst[index] > n:
            count += 1
        
        index += 1

    return count

def solution(lst):

    for i in range(1, N + 1):
        if countHigh(lst, i) != p[i - 1]:
            return False
    
    return True

N = int(input())
p = list(map(int,input().split()))

for lst in permutations([i for i in range(1, N+1)], N):
    if solution(lst):
        print(*lst)
        break