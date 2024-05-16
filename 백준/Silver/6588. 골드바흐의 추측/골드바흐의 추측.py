import sys
input = sys.stdin.readline

max=1000000
goldbah=[True]*(max+1)

k=2
while k*k<=max:
    if goldbah[k]:
        for i in range(k*k,max,k):
            goldbah[i]=False
    k+=1
goldbah[0]=False
goldbah[1]=False


while True:
    a=int(input().strip())
    if a==0:
        break
    else:
        for i in range(2,a):
            if goldbah[i] and goldbah [a-i]:
                print(f"{a} = {str(i)} + {str(a-i)}")
                break

