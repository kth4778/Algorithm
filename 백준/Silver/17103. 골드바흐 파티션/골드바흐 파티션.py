def solution(n):
    sosu_list=[True]*(n+1)
    p=2
    while p*p<=n:
        if sosu_list[p]:
            for i in range(p*p,n+1,p):
                sosu_list[i]=False
        p+=1
    return sosu_list
a=int(input())
b=[int(input()) for _ in range(a)]
max_num=max(b)
max_sosu_list=solution(max_num)
count_list=[0 for _ in range(len(b))]

for index,i in enumerate(b):
    for w in range(2,i//2+1):
        if max_sosu_list[w] and max_sosu_list[i-w]:
            count_list[index]+=1        
for i in count_list:
    print(i)