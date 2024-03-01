score={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,
       'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
a=[['TEST']]
w=[]
u=0
t=['pass',0,'F']
for i in range(1,21):
    b=list(input().split())
    if b[2]!='P':
        a.append(b)
        u+=float(a[i][1])
        c=a[i][2]
        p=(score[c]*float(a[i][1]))
        w.append(p)
    else:
        a.append(t)
print(sum(w)/u)