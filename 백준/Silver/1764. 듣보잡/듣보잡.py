from collections import Counter

a,b=map(int,input().split())
see=sorted([input() for _ in range(a+b)])
result=[key for key,value in dict(Counter(see)).items() if value==2]
print(len(result))
for i in result:
    print(i) 
