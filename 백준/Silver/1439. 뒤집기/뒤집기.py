a=input()

switch=1
result=[]
for i in a:
    if not result:
        result.append(i)
    else:
        if result[-1]!=i:
            result.append(i)
            switch+=1
if switch%2==0:
    print(switch//2)
else:
    print((switch-1)//2)