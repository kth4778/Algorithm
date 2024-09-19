from itertools import permutations

n = int(input())
for comb in permutations([i for i in range(1, n+1)], n):
    print(' '.join([str(j) for j in comb]))