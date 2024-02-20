a,b=map(int,input().split())
c=(a*60+b)-45
d=c+1440
if 0<=a<=23 and 0<=b<=59 and c<0:
    print(d//60,d%60)
elif 0<=a<=23 and 0<=b<=59 and c>=0:
    print(c//60,c%60)

