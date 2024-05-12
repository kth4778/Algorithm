a=int(input())
b=int(input())
c=int(input())
result=[a,b,c]
ansewer=[None,'Equilateral','Isosceles','Scalene']
if sum(result)==180:
    print(ansewer[len(set(result))])
else:
    print('Error')