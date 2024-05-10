a=int(input())
result=[]
p=2
if a==1:
    pass
else:
    while a>1:
        if a%p==0:
            a//=p
            print(p)
        else:
            p+=1