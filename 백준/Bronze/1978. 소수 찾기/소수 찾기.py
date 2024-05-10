a=input()
b=list(map(int,input().split()))
b=[i for i in b if i>1]
result=0
for i in b:
    list_bar=[]
    for w in range(2,int(i**0.5)+1):
        if i%w==0:
            list_bar.append(w)
    else:
        if not list_bar:
            result+=1
print(result)
