while True:
    a,b=input().split()
    a=int(a)
    b=int(b)
    if a==0 and b==0:
        break
    if a>b and float(a/b).is_integer():
        print('multiple')
    elif a<b and float(b/a).is_integer():
        print('factor')
    else:
        print('neither')