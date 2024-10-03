N, K = map(int,input().split())
table = [0 for _ in range(K + 1)]

for _ in range(N):
    w,v = map(int,input().split())
    if w > K:
        continue
    for i in range(K, 0, -1):
        if table[i] != 0 and i + w <= K:
            table[i + w] = max(table[i + w], table[i] + v)
    table[w] = max(table[w], v)
print(max(table))