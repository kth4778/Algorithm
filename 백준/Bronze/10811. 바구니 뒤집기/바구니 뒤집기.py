a,b=map(int,input().split())
box=list(range(1,a+1))
for i in range(b):
    c,d=map(int,input().split())
    box[c-1:d]=box[c-1:d][::-1]
print(*box)