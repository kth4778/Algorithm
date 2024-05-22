a=input()
string_dict={}
for i in a:
    if i not in string_dict:
        string_dict[i]=1
    else:
        string_dict[i]+=1

if len(a)%2==0:
    b=[i%2==0 for i in string_dict.values()]
    if not all(b):
        print('I\'m Sorry Hansoo')
    else:
        result=''
        for i in sorted(string_dict):
            result+=i*(string_dict[i]//2)
        print(result+result[::-1])

else:
    count=0
    for i in string_dict.values():
        if i%2!=0:
            count+=1
    if count!=1:
        print('I\'m Sorry Hansoo')
    else:
        result=''
        hols=''.join([w for w in sorted(string_dict) if string_dict[w]%2!=0])
        string_dict[hols]-=1
        for i in sorted([w for w in string_dict if string_dict!=0]):
            result+=i*(string_dict[i]//2)
        print(result+hols+result[::-1])
    
