def solution(n):
    k=1
    count=0
    while k*k<=n:
        k+=1
        count+=1
    return count
print(solution(int(input())))