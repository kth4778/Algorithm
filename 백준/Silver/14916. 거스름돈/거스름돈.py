a=int(input())
if a==1 or a==3:
    print(-1)
else:
    if a%5==0:
        print(a//5)
    elif (a%5)%2==0:
        print(a//5+(a%5)//2)
    elif (a%5)%2!=0:
        count=0
        while True:
            a-=2
            count+=1
            if a%5==0:
                count+=a//5
                break
        print(count)

