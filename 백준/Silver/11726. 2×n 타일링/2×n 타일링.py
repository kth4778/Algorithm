a=int(input())
result=[0,1]
for i in range(a):
    result[1],result[0]=sum(result),result[1]
print(result[1]%10007)
