from itertools import combinations
b=[int(input()) for _ in range(9)]
result=[]
for i in combinations(b,7):
    if sum(i)==100:
        for w in sorted(i):
            print(w)
        break