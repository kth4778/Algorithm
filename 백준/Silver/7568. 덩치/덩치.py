a=int(input())
result=[list(map(int,input().split())) for _ in range(a)]
body_rank=[1 for _ in range(a)]
for i in range(a):
    for w in range(i,a):
        if result[i][0]<result[w][0] and result[i][1]<result[w][1]:
            body_rank[i]+=1
        elif result[i][0]>result[w][0] and result[i][1]>result[w][1]:
            body_rank[w]+=1
print(' '.join([str(i) for i in body_rank]))