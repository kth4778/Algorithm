n = int(input())
lst = list(map(int,input().split()))

que = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]  and que[i] <= que[j]:
            que[i] = que[j]+1

print(max(que)) 