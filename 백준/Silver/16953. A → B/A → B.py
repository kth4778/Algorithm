a,b=map(int,input().split())
count=1
while a!=b:
    if str(b)[-1]=='1':
        b//=10
        count+=1
    elif b%2==0 and b>0:
        b//=2
        count+=1
    else:
        count=-1
        break
print(count)