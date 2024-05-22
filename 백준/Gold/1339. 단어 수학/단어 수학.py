a=int(input())
alphabat_dict={}
result=[]
for i in range(a):
    st=input()
    result.append(st)
    for i in range(len(st)):
        if st[i] not in alphabat_dict:
            alphabat_dict[st[i]]=10**(len(st)-i)
        else:
            alphabat_dict[st[i]]+=10**(len(st)-i)
alphabat_dict=dict(sorted(alphabat_dict.items(),key=lambda x:x[1],reverse=True))
num=9
for i in alphabat_dict:
    alphabat_dict[i]=num
    num-=1

count=0
for i in result:
    length=len(i)
    for w in range(length):
        count+=alphabat_dict[i[w]]*(10**(length-w-1))
print(count)
