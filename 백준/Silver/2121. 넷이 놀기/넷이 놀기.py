a=int(input())
x,y=map(int,input().split())
count=0
coordinate=set(tuple(map(int, input().split())) for _ in range(a))
for q,w in coordinate:
    if (q+x,w) in coordinate and (q,w+y) in coordinate and (q+x,w+y) in coordinate:
        count+=1
print(count)