import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
nums_idx = [i for i in range(n+1)]

def find(x):
    if x == nums_idx[x]:
        return x
    nums_idx[x] = find(nums_idx[x])
    return nums_idx[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 
    if x > y:
        nums_idx[x] = y
    else:
        nums_idx[y] = x

for _ in range(m):
    t,a,b = map(int,input().split())
    if t == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")