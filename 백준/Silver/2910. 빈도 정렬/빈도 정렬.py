from collections import Counter

N,C = map(int,input().split())
p = list(map(int,input().split()))
l = Counter(p)

p = sorted(p, key = lambda x : (l[x], -p.index(x)), reverse = True)
for i in p:
    print(i, end = " ")