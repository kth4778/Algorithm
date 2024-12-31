T = int(input())

for _ in range(T):
    r,e,c = map(int,input().split())

    a = e - c
    b = r

    if a == b:
        print('does not matter')
    elif a > b:
        print('advertise')
    else:
        print('do not advertise')