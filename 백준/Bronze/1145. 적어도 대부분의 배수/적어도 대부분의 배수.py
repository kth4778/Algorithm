def solution(lst,num):
    count=0
    for i in lst:
        if num//i == num/i:
            count+=1
    return count
a=list(map(int,input().split()))
min_num=min(a)
while True:
    if solution(a,min_num)>=3:
        print(min_num)
        break
    else:
        min_num+=1
