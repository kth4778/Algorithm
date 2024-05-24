a=int(input())
for _ in range(a):
    h,w,n=map(int,input().split())
    hotel=[100*i for i in range(1,h+1)]
    result=[i+p for p in range(1,w+1) for i in hotel ]
    print(result[n-1])