from collections import Counter
a=list(input().lower())
b=dict(Counter(a))

c=max(b.values())
d=[key for key,value in b.items() if value==c]
e=[fat.upper() for fat in d]
if len(d)==1:
    print(*e)
elif len(d)>1:
    print('?')