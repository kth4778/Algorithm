def factorial(num):
    result=1
    for i in range(1,num+1):
        result*=i
    return result
a=int(input())
count=0
for i in str(factorial(a))[::-1]:
    if i=='0':
        count+=1
    else:
        break
print(count)