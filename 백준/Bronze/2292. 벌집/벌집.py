a=int(input())
if a==1:
    print(1)
else:
    a=a-1
    result=2
    for i in range(1,10000000):
        if a-6*i>0:
            result+=1
            a-=6*i
        else:
            print(result)
            break