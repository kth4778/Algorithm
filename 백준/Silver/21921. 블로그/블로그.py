N,X = map(int,input().split())
days = list(map(int,input().split()))

cur = sum(days[:X])
max_visited = sum(days[:X])
p = 1

for i in range(X, N):
    cur -= days[i - X]
    cur += days[i]

    if cur > max_visited:
        max_visited = cur
        p = 1
    elif cur == max_visited:
        p += 1
    

if max_visited == 0:
    print("SAD")
else:
    print(max_visited)
    print(p)