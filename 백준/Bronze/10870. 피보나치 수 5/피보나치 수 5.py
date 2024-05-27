def solution(a):
    result=[0,1]
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        for i in range(a-2):
            b=sum(result)
            result[0]=result[1]
            result[1]=b
        return sum(result)
a=int(input())
print(solution(a))