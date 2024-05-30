a=int(input())
result=[0 for _ in range(a+1)]
for i in range(2,a+1):
    result[i]=1+result[i-1]
    if i%2==0:
        result[i]=min(result[i],1+result[i//2])
    if i%3==0:
        result[i]=min(result[i],1+result[i//3])
print(result[-1])