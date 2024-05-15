a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))

result={i:1 for i in b}

for i in d:
    try:
        print(result[i])
    except:
        print(0)