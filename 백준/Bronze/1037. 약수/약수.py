a=int(input())
b=list(map(int,input().split()))
c=sorted(b)
print(c[0]*c[-1])