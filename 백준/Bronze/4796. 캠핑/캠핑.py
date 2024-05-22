num=1
while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        count=c//b*a
        if c%b>a:
            count+=a
        else:
            count+=c%b
        print(f'Case {num}: {count}')
        num+=1