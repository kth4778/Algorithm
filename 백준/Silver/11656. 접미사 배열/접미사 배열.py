s = input()

for p in sorted([s[i:] for i in range(len(s))]):
    print(p)