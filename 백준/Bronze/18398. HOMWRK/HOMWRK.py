T = int(input())

for _ in range(T):
    N = int(input())
    for _ in range(N):
        a, b = map(int,input().split())
        print(f"{a + b} {a * b}")