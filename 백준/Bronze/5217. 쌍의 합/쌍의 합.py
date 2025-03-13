t = int(input())

for _ in range(t):
    switch = True
    n = int(input())
    p = f"Pairs for {n}:"
    for i in range(1, n // 2 + 1):
        if i < n - i:
            if switch:
                p += " " + str(i) + " " + str(n - i)
                switch = False
            else:
                p += ", " + str(i) + " " + str(n - i)
    print(p)
        