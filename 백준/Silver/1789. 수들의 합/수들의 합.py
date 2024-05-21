a=int(input())
count=0
set_num=1
while True:
    count+=set_num
    if count>a:
        break
    set_num+=1
print(set_num-1)