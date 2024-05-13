a=int(input())
result=[]
for _ in range(a):
    result.append(input())
result=list(set(result))
for i in sorted(sorted(result),key=lambda x:len(x)):
    print(i)