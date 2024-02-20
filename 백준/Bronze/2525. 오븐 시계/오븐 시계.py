a,b=map(int,input().split())
c=int(input())
d=a*60+b+c
if 0<d<1440:
    print(d//60,d%60)
elif 1440<d<2880:
    print((d-1440)//60,(d-1440)%60)
elif 1440==d:
    print(0,0)