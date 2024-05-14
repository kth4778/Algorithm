import sys
input = sys.stdin.readline

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

a=int(input())
result=[]
for _ in range(a):
    result.append(int(input()))
result.sort()

tree_distance=[]
for i in range(1,len(result)):
    tree_distance.append(result[i]-result[i-1])

r=2
tree_gcd=gcd(tree_distance[0],tree_distance[1])
while r<len(tree_distance):
    tree_gcd=gcd(tree_gcd,tree_distance[r])
    r+=1


print((result[-1]-result[0])//tree_gcd+1-len(result))
