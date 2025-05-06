N = int(input())

t = [list(input().split()) for _ in range(N)]
t.sort(key = lambda x : x[1])
print(t[0][0])