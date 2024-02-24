import string
a=string.ascii_lowercase
b={i:-1 for i in a}
c=input()
for index,o in enumerate(c):
    if b[o]==-1:
        b[o]=index
r=list(b.values())
print(*r)