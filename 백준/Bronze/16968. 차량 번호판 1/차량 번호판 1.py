a = input()
result = []
for i in a:
    if not result:
        result.append([i,1])
    else:
        if result[-1][0]==i:
            result[-1][1]+=1
        else:
            result.append([i,1])
num = 1
for i in result:
    if i[0]=='d':
        p=0
        for w in range(i[1]):
            if p == 0:
                num*=10
            else:
                num*=9
            p+=1
    elif i[0]=='c':
        p=0
        for w in range(i[1]):
            if p == 0:
                num*=26
            else:
                num*=25
            p+=1
print(num)