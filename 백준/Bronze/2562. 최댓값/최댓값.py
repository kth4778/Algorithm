b=[]
for i in range(9):
    a=int(input())
    if type(a)==int:
        b.append(a)
print(max(b))
print((b.index(max(b)))+1)