from math import ceil
a,b,v=map(int,input().split())
v-=a
result=ceil(v/(a-b))+1
print(result)