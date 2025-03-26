a,b = 0,1

n = int(input())

for _ in range(n - 1):
    a,b = b, a + b

print(b)