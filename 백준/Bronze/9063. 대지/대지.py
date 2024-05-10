a=int(input())
x_ran=[]
y_ran=[]
for _ in range(a):
    q,w=map(int,input().split())
    x_ran.append(q)
    y_ran.append(w)
print((max(x_ran)-min(x_ran))*(max(y_ran)-min(y_ran)))