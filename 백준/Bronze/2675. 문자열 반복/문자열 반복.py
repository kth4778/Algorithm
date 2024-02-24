a=int(input())
my_list=[]
for i in range(a):
    my_list.append(list(input().split()))
for i in range(a):
    print(''.join(char * int(my_list[i][0]) for char in my_list[i][1]))