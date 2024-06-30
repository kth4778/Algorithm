from math import gcd

t = int(input())

def solution(m,n,x,y):
    if x<=y:
        i = x
        while i <= m*n:
            if i%n == 0:
                t1 = n
            else:
                t1 = i%n
            
            if t1 == y:
                return i
            
            i+=m

    elif x>y:
        i = y
        while i <= m*n:
            if i%m == 0:
                t1 = m
            else:
                t1 = i%m
            
            if t1 == x:
                return i
            
            i+=n  


    return -1

result = []
for _ in range(t):
    m,n,x,y = map(int,input().split())
    if m==x and n==y:
        print(m*n//(gcd(m,n)))
    else:
        print((solution(m,n,x,y)))
