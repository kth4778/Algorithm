a=input().split('.')
result=''
switch=True

for i in a:
    if int(not i) == switch:
        result+='.'
    else:
        if len(i)%2==0:
            result+=len(i)//4*'AAAA'+len(i)%4//2*'BB'
            result+='.'
        else:
            result=''
            break
if not result:
    print(-1)
elif result[-1]=='.':
    print(result[:-1])
else:
    print(result)