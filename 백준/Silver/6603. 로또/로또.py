from itertools import combinations

while True:
    lotto = list(map(int,input().split()))
    if lotto[0] == 0:
        exit()
    for i in combinations(lotto[1:],6):
        print(*i)
    print()