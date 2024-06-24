n,c,r = map(int,input().split())
cnt=0
while n>0:
    n-=1
    if c>=2**n and r>=2**n:
        c-=2**n
        r-=2**n
        cnt+=(2**n)*(2**n)*3
    elif c>=2**n and r<2**n:
        c-=2**n
        cnt+=(2**n)*(2**n)*2
    elif c<2**n and r>=2**n:
        r-=2**n
        cnt+=(2**n)*(2**n)*1
    else:
        pass
print(cnt)