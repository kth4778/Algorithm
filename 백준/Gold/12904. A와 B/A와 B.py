s=input()
t=input()

length=len(t)-len(s)
for _ in range(length):
    if t[-1]=='A':
        t=t[:-1]
    elif t[-1]=='B':
        t=t[:-1]
        t=t[::-1]
if s==t:
    print(1)
else:
    print(0)