a=int(input())
def common_measure(a,b):
    set_num=0
    for i in range(1,min([a,b])+1):
        if a%i==0 and b%i==0:
            set_num=i
    return set_num
for _ in range(a):
    q,w=map(int,input().split())
    nanu=common_measure(q,w)
    print(nanu*q//nanu*w//nanu)
