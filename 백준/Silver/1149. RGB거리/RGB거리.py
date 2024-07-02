def solution(a,b,homes):
    idx = homes[a].index

n = int(input())
homes = [list(map(int,input().split())) for _ in range(n)]
if n == 1:
    print(min(homes[0]))
else:
    set_lst = homes[0]
    for i in range(1,n):
        idx1 = set_lst.index(min(set_lst))
        s = min([set_lst[i] for i in set([0,1,2])-set([idx1])])
        if idx1 == 0:
            set_lst = [homes[i][0]+s,homes[i][1]+set_lst[0],homes[i][2]+set_lst[0]]
        elif idx1 == 1:
            set_lst = [homes[i][0]+set_lst[1],homes[i][1]+s,homes[i][2]+set_lst[1]]
        else:
            set_lst = [homes[i][0]+set_lst[2],homes[i][1]+set_lst[2],homes[i][2]+s]
    print(min(set_lst))