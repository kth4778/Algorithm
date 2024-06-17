import sys
input = sys.stdin.readline
import heapq

t=int(input())
for _ in range(t):
    k=int(input())
    max_que=[]
    min_que=[]
    que_dict={}
    for _ in range(k):
        a,b=input().split()
        if a=='I':
            heapq.heappush(max_que,-1*int(b))
            heapq.heappush(min_que,int(b))
            if int(b) not in que_dict:
                que_dict[int(b)]=1
            else:
                que_dict[int(b)]+=1
        elif a=='D':
            if b=='-1':
                while min_que and que_dict[min_que[0]]==0:
                    heapq.heappop(min_que)
                    if not min_que:
                        break
                if min_que:
                    p=heapq.heappop(min_que)
                    que_dict[p]-=1
            if b=='1':
                while max_que and que_dict[max_que[0]*-1]==0:
                    heapq.heappop(max_que)
                    if not max_que:
                        break
                if max_que:
                    p=heapq.heappop(max_que)
                    que_dict[p*-1]-=1
    while max_que and que_dict[max_que[0]*-1]==0:
        heapq.heappop(max_que)
        if not max_que:
            break
    while min_que and que_dict[min_que[0]]==0:
        heapq.heappop(min_que)
        if not min_que:
            break
    if min_que and max_que:
        print(max_que[0]*-1,min_que[0])
    else:
        print('EMPTY')