n = int(input())

min_lst = None
max_lst = None

for i in range(n):
    m = list(map(int,input().split()))
    if i == 0:
        min_lst = m.copy()
        max_lst = m.copy()
    else:
        new_min_lst = [0,0,0]
        new_max_lst = [0,0,0]

        new_min_lst[0] = min(min_lst[0], min_lst[1]) + m[0]
        new_max_lst[0] = max(max_lst[0], max_lst[1]) + m[0]

        new_min_lst[1] = min(min_lst[0], min_lst[1], min_lst[2]) + m[1]
        new_max_lst[1] = max(max_lst[0], max_lst[1], max_lst[2]) + m[1]

        new_min_lst[2] = min(min_lst[1], min_lst[2]) + m[2]
        new_max_lst[2] = max(max_lst[1], max_lst[2]) + m[2]

        min_lst = new_min_lst
        max_lst = new_max_lst

print(max(max_lst),min(min_lst))