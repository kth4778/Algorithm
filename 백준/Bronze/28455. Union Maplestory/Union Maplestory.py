n = int(input())

a = 0
b = 0

L = sorted([int(input()) for _ in range(n)], reverse = True)

for l in L[:42]:
    if l >= 250:
        b += 5
    elif l >= 200:
        b += 4
    elif l >= 140:
        b += 3
    elif l >= 100:
        b += 2
    elif l >= 60:
        b += 1
    
    a += l

print(f"{a} {b}")