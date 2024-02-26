a=int(input())
for i in range(1,a+1):
    q=a-i
    w=2*i-1
    print(' '*q+'*'*w)
for y in range(a-1,0,-1):
    q=a-y
    w=2*y-1
    print(' '*q+'*'*w)