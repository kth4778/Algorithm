a,b=map(int,input().split())
min_num=min([a,b])
c=max([i for i in range(1,min_num+1) if a%i==0 and b%i==0])
d=a//c*b//c*c
print(c,d)