import sys
input = sys.stdin.readline

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parents[a] = b
    else:
        parents[b] = a

G = int(input())
P = int(input())
airplane = [int(input()) for _ in range(P)]
parents = [i for i in range(G + 1)]
answer = 0

for x in airplane:
    x = find(x)
    if x == 0:
        break

    union(x, x - 1)
    answer += 1

print(answer)