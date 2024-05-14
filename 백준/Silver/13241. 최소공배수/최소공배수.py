def sosu(a,b):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    for i in range(2,int(b**0.5)+1):
        if b%i==0:
            return False
    return True
def common_measure(a,b):
    set_num=0
    for i in range(1,min([a,b])+1):
        if a%i==0 and b%i==0:
            set_num=i
    return set_num


q,w=map(int,input().split())
if sosu(q,w):
    print(q*w)
else:
    nanu=common_measure(q,w)
    print(nanu*q//nanu*w//nanu)