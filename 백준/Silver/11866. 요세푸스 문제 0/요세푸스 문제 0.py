n,k=map(int,input().split())
a=[i for i in range(1,n+1)]
result=[]
index=0
for _ in range(n):
    index=(index+k-1)%len(a)
    result.append(a.pop(index))
result=str(result)
result=result.replace('[','<')
result=result.replace(']','>')
print(result)