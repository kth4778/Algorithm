import sys
input = sys.stdin.readline

def gcd(q,w):
    while w!=0:
        q,w=w,q%w
    return q

a,b=map(int,input().split())
c,d=map(int,input().split())
x=a*d+c*b
y=b*d

result=gcd(x,y)
print(x//result,y//result)
