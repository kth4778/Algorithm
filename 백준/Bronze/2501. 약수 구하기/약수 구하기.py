a,b=map(int,input().split())
N=[i for i in range(1,a+1) if a%i==0]
if len(N)>=b:
    print(N[b-1])
else:
    print(0)