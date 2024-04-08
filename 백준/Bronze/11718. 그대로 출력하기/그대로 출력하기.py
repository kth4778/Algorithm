while True:
    try:
        a=input()
        if a[0]!=' ' and a[-1]!=' ':
            print(a)
        else:
            break
    except:
        break