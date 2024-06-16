n = int(input())
num_list = list(map(int, input().split()))
que = {num_list[0]: [1]}
count_num = []
set_num2 = num_list[0]

for i in range(1,len(num_list)):
    if len(que) == 1:
        if num_list[i] in que:
            que[num_list[i]][-1] += 1
        else:
            que[num_list[i]] = [1]
            set_num2 = num_list[i]
    else:
        if num_list[i] in que:
            if num_list[i] == set_num2:
                que[num_list[i]][-1] += 1
            else:
                que[num_list[i]].append(1)
                set_num2 = num_list[i]
        else:
            count_num.append(sum([sum(p) for p in que.values()]))
            del que[[w for w in que.keys() if w!=num_list[i-1]][0]]
            que[list(que.keys())[0]]=[que[list(que.keys())[0]][-1]]
            set_num2 = num_list[i]
            que[num_list[i]]=[1]
count_num.append(sum([sum(p) for p in que.values()]))
print(max(count_num))
