paper_count=int(input())
coordinate=[]
for _ in range(paper_count):
    coordinate.append(list(map(int,input().split())))
x_coordinate=[i[0] for i in coordinate]
y_coordinate=[i[1] for i in coordinate]

a=[[0]*(max(x_coordinate)+10) for i in range(max(y_coordinate)+10)]
for i in coordinate:
    for w in range(i[0],i[0]+10):
        for p in range(i[1],i[1]+10):
            a[p][w]=1
b=0
for i in a:
    b+=i.count(1)
print(b)