a=int(input())
money=[25,10,5,1]
for i in range(a):
    result=int(input())
    a=[]
    for i in money:
        a.append(result//i)
        result=result-result//i*i
    print(' '.join(map(str,a)))
    a=[]
        
