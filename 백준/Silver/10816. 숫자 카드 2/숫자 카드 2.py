from collections import Counter

a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))
result=dict(Counter(b))
solution=[]

for i in d:
    try:
        solution.append(str(result[i]))
    except:
        solution.append('0')
print(' '.join(solution))