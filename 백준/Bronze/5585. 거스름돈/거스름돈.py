count=0
a=int(input())
result=1000-a
while result>0:
    for i in [500,100,50,10,5,1]:
        if result//i!=0:
            count+=result//i
            result%=i
print(count)