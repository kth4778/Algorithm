N = int(input())
num_list = sorted(list(map(int,input().split())))

smallest_num = 1

for num in num_list:
    if num > smallest_num:
        break
    smallest_num += num

print(smallest_num)