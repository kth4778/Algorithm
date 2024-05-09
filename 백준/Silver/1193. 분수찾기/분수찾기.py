a=int(input())
b=1
while True:
    a-=b
    if a<=0:
        break
    b+=1
result=[i for i in range(1,b+1)]
num1=result[a+b-1]
num2=result[::-1][a+b-1]
if b%2==0:
    print(f"{num1}/{num2}")
else:
    print(f"{num2}/{num1}")