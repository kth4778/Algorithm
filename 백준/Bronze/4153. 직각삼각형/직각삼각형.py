while True:
    a=sorted(list(map(int,input().split())))
    if a[0]==0:
        break
    else:
        answer=['wrong','right']
        print(answer[a[0]**2+a[1]**2==a[2]**2])