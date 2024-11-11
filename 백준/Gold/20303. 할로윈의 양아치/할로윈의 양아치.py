import sys
input = sys.stdin.readline

def find(x):
    if childs_info[x] != x:
        childs_info[x] = find(childs_info[x])
    return childs_info[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        childs_info[a] = b
    else:
        childs_info[b] = a

N,M,K = map(int,input().split())
childs = list(map(int,input().split()))
childs_info = {i:i for i in range(1, N + 1)}

for _ in range(M):
    a,b = map(int,input().split())
    union(a,b)

for i in range(1, N + 1):
    find(i)

friends = {i:[0,0] for i in set(childs_info.values())}

for i in range(1, N + 1):
    friends[childs_info[i]][0] += 1
    friends[childs_info[i]][1] += childs[i - 1]

dp = [0 for _ in range(K)] 

for count, score in friends.values():
    for i in range(K - 1, -1, -1):
        if dp[i] != 0:
            if count + i < K:
                dp[count + i] = max(dp[count + i], dp[i] + score)
    if count < K:
        dp[count] = max(score, dp[count])
print(max(dp))