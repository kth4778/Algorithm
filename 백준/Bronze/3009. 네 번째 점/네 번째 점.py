result_x=[]
result_y=[]
last_result=[]
for _ in range(3):
    a,b=map(int,input().split())
    result_x.append(a)
    result_y.append(b)
    last_result.append([a,b])
result_x=set(result_x)
result_y=set(result_y)
x1=result_x.pop()
x2=result_x.pop()
y1=result_y.pop()
y2=result_y.pop()

c=[[x1,y1],[x1,y2],[x2,y1],[x2,y2]]
for i in c:
    if i not in last_result:
        print(i[0],i[1])