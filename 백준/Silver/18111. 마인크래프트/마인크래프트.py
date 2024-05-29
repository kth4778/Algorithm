import sys
input = sys.stdin.readline

a,b,c=map(int,input().split())
if a==1 and b==1:
    p=int(input())
    print(0,p)
else:
    block=[]

    for _ in range(a):
        block.extend([i for i in list(map(int,input().split()))])
    block.sort()   #O(n)

    min_block=block[0]    #O(n)
    max_block=block[-1]    #O(n)
    result=[[0,0,0] for _ in range(max_block-min_block+1)]  #O(n) [걸리는 시간,블럭소모개수,땅의 높이]
    if max_block<=256:
        for index,i in enumerate(range(min_block,max_block+1)): #O()
            result[index][2]=i
            for w in block:
                if i>w:
                    result[index][0]+=i-w
                    result[index][1]+=i-w
                elif i<w:
                    result[index][0]+=(w-i)*2
                    result[index][1]-=w-i
    else:
        for index,i in enumerate(range(min_block,257)): #O()
            result[index][2]=i
            for w in block:
                if i>w:
                    result[index][0]+=i-w
                    result[index][1]+=i-w
                elif i<w:
                    result[index][0]+=(w-i)*2
                    result[index][1]-=w-i

    last_result=[i for i in result if i[1]<=c]
    last_result.sort()

    min_time=last_result[0][0]

    retu=[i for i in last_result if i[0]==min_time]
    retu=sorted(retu,key=lambda x:x[2],reverse=True)
    print(retu[0][0],retu[0][2])
