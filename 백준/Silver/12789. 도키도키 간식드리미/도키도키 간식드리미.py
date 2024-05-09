a=int(input())
b=list(map(int,input().split()))

count_num=1
waiting_list=[]

for i in b:
    if i==count_num:
        count_num+=1
        while True:
            if waiting_list and waiting_list[-1]==count_num:
                waiting_list.pop()
                count_num+=1
            else:
                break
    else:
        waiting_list.append(i)

result=['Sad','Nice']

print(result[int(not waiting_list)])