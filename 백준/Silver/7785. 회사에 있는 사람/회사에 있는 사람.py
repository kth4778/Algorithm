import sys
input = sys.stdin.readline

company_people={}
a=int(input())

for _ in range(a):
    a,b=input().split()
    if b=='enter':
        company_people[a]=1
    else:
        company_people[a]=0
b=sorted(company_people,reverse=True)
for i in b:
    if company_people[i]==1:
        print(i)