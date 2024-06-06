import sys
input = sys.stdin.readline
result=[]
M=int(input())
empty_set=set()
for _ in range(M):
    a=input().strip().split()
    if a[0]=='add':
        empty_set.add(a[1])
    elif a[0]=='remove':
        if a[1] in empty_set:
            empty_set.remove(a[1])
    elif a[0]=='check':
        if a[1] in empty_set:
            print(1)
        else:
            print(0)
    elif a[0]=='toggle':
        if a[1] in empty_set:
            empty_set.remove(a[1])
        else:
            empty_set.add(a[1])
    elif a[0]=='all':
        empty_set=set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])
    elif a[0]=='empty':
        empty_set=set()