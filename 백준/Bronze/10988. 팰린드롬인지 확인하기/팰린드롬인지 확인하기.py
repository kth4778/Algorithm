a=input()
b=a.lower()
if b[::-1]==b:
    print(1)
elif b[::-1]!=b:
    print(0)