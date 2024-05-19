a,b=map(int,input().split())
coins=sorted([int(input()) for _ in range(a)],reverse=True)
count=0
for i in coins:
    if b//i>0:
        count+=b//i
        b=b%i
print(count)   
