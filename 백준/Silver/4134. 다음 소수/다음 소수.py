def sosu(a):
    if a<2:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

length=int(input())
for _ in range(length):
    p=int(input())
    while True:
        if sosu(p):
            print(p)
            break
        else:
            p+=1