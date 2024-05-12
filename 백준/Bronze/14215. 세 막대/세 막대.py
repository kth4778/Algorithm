a,b,c=map(int,input().split())
result=sorted([a,b,c])
if sum(result[:-1])>result[-1]:
    print(sum(result))
else:
    print(sum(result[:-1])*2-1)