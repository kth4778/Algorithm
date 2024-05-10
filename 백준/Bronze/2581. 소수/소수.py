a=int(input())
b=int(input())

result=[i for i in range(a,b+1) if i>=2]
solution=[]

for i in result:
    sosu_list=[]
    for w in range(2,i):
        if i%w==0:
            sosu_list.append(w)
            break
    else:
        if not sosu_list:
            solution.append(i)
        else:
            pass
if solution:
    print(sum(solution))
    print(solution[0])
else:
    print(-1)