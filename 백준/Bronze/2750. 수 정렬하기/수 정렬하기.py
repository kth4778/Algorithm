a=int(input())
nums_list=[]
for _ in range(a):
    nums_list.append(int(input()))
for i in sorted(nums_list):
    print(i)