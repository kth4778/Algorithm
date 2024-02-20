a=input()
b=list(map(int,a.split()))
q=b[0]
w=b[1]
e=b[2]
if q==w==e:
    print(10000+q*1000)
elif len(set(b)) == 2:
    for num in set(b):
        if b.count(num) == 2:
            print(1000+num * 100)
            break
elif q!=w!=e:
    print(100*max(b))