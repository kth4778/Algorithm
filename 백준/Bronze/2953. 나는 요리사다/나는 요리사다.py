a=[sum(list(map(int,input().split()))) for _ in range(5)]
p=max(a)
print(f"{a.index(p)+1} {p}")