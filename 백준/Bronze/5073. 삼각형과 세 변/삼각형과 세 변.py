while True:
    a,b,c=map(int,input().split())
    result=sorted([a,b,c])
    answer=[None,'Equilateral','Isosceles','Scalene']
    if sum(result)==0:
        break
    else:
        if sum(result[:-1])<=result[-1]:
            print('Invalid')
        else:
            print(answer[len(set(result))])