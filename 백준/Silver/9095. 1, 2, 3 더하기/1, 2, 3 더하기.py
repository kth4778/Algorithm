from itertools import product
p=int(input())
re=[]
for _ in range(p):
    num=int(input())
    a=[1,2,3]
    count=0
    for i in range(1,num+1):
        for w in list(product(a,repeat=i)):
            if sum(w)==num:
                count+=1
    print(count)