a=int(input())
for i in range(a):
    b=str(i)
    if i+sum([int(w) for w in b])==a:
        print(i)
        break
else:
    print(0)