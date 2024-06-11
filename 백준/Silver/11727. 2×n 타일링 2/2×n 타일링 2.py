wide=1
a=int(input())
for i in range(1,a+1):
    if i%2==0:
        wide*=2
        wide+=1
    elif i%2==1:
        wide*=2
        wide-=1

print(wide%10007)
