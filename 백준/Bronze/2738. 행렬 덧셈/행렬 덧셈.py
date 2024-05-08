n,m=map(int,input().split())
list1=[[] for _ in range(n)]
list2=[[] for _ in range(n)]
for i in range(n):
    list1[i].extend(list(map(int,input().split())))
for i in range(n):
    list2[i].extend(list(map(int,input().split())))
result=[[] for _ in range(n)]
for index,i in enumerate(zip(list1,list2)):
    for w in range(m):
        result[index].append(i[0][w]+i[1][w])
for i in result:
    print(' '.join(map(str,i)))