a=int(input())
b=[input() for i in range(a)]
ap=[[] for i in range(a)]
for i in range(a):
    for w in b[i]:
        if w not in ap[i] or ap[i][-1] == w:
            ap[i].append(w)
        else:
            pass
c=sum([1 for i in range(a) if ''.join(ap[i])==b[i]])
print(c)