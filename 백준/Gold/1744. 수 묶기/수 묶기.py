a=int(input())
plus=[]
minus=[]
count=0
zero=False

for _ in range(a):
    num=int(input())

    if num>1:
        plus.append(num)
    elif num<0:
        minus.append(num)
    elif num==1:
        count+=1
    else:
        zero=True

plus=sorted(plus,reverse=True)
minus=sorted(minus)

if len(plus)%2==0:
    for i in range(0,len(plus),2):
        count+=plus[i]*plus[i+1]
else:
    for i in range(0,len(plus)-1,2):
        count+=plus[i]*plus[i+1]
    count+=plus[-1]

if len(minus)%2==0:
    for i in range(0,len(minus),2):
        count+=minus[i]*minus[i+1]
else:
    for i in range(0,len(minus)-1,2):
        count+=minus[i]*minus[i+1]
    if zero:
        count+=0
    else:
        count+=minus[-1]
print(count)