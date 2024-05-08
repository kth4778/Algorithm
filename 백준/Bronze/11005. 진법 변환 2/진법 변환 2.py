B,N=map(int,input().split())
alphabat_dict={str(i+10):chr(i+65) for i in range(26)}
for i in range(10):
    alphabat_dict[str(i)]=i

result=[]
while True:
    if B//N!=0:
        result.extend(str(alphabat_dict[str(B%N)]))
        B//=N
    else:
        result.extend(str(alphabat_dict[str(B)]))
        break
   
print(''.join(result[::-1]))