def sosu(a):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
result={i:sosu(i) for i in range(2,123456*2+1)}
result[1]=False
while True:
    p=int(input())
    k=0
    if p==0:
        break
    else:
        for i in range(p+1,2*p+1):
            if result[i]:
                k+=1
        print(k)