from collections import Counter

n = int(input())
p = dict(Counter([int(input()) for _ in range(n)]))
p = sorted(p, key = lambda x:(-p[x], x))
print(p[0])