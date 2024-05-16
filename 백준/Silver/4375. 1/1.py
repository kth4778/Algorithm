while True:
    try:
        num=1
        a=int(input())
        while True:
            if num%a!=0:
                num=num*10+1
            else:
                break
        print(len(str(num)))
    except:
        break