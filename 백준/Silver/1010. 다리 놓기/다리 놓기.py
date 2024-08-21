t = int(input())

def answer(a,b):
    result = 1
    for _ in range(a):
        result *= b
        b -= 1
    p = 1
    for i in range(a):
        p *= (i+1)
    return result // p

for _ in range(t):
    a,b = map(int,input().split())
    print(answer(a,b))