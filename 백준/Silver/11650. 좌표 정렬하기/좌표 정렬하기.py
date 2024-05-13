a=int(input())
result=[]
for _ in range(a):
    result.append(list(map(int,input().split())))
for a,b in sorted(result):
    print(a,b)