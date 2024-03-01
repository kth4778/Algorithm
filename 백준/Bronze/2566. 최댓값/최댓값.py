lists=[[] for i in range(9)]
a=[]

for i in range(9):
    w=list(map(int,input().split()))
    lists[i]=w
for i in range(9):
    a.append(max(lists[i]))
print(max(a))
w=a.index(max(a))
print(w+1,lists[w].index(max(a))+1)