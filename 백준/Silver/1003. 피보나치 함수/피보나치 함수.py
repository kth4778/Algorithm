t=int(input())
for i in range(t):
    n=int(input())
    lst=[1,0]
    for w in range(n):
        set=sum(lst)
        lst[0]=lst[1]
        lst[1]=set
    print(' '.join([str(p) for p in lst]))
    