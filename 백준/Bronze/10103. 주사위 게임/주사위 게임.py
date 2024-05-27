a=int(input())
result=[100,100]

for i in range(a):
    q,w=map(int,input().split())
    if q>w:
        result[1]-=q
    elif q<w:
        result[0]-=w
print(result[0])
print(result[1])