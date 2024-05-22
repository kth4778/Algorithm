import sys
input = sys.stdin.readline

money,a=map(int,input().split())
package=[]
package2=[]

for _ in range(a):
    p,q=map(int,input().split())
    package.append(q)
    package2.append(p)
    package2.append(q*6)
result=[]
result.append(min(package)*money)
result.append(min(package2)*(money//6+1))
result.append(min(package2)*(money//6)+min(package)*(money%6))
print(min(result))
