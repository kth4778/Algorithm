while True:
    a=int(input())
    answer=['no','yes']
    if a==0:
        break
    else:
        print(answer[int(str(a)==str(a)[::-1])])