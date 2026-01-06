import heapq

T = int(input())

for _ in range(T):
    K = int(input())
    max_que = []
    min_que = []
    is_delete = [False for _ in range(K)]
    
    for i in range(K):
        o,n = input().split()
        n = int(n)

        if o == 'I':
            heapq.heappush(max_que, (-n, i))
            heapq.heappush(min_que, (n, i))
        else:
            if n == 1:
                while max_que and is_delete[max_que[0][1]]:
                    heapq.heappop(max_que)
                
                if max_que:
                    num, index = heapq.heappop(max_que)
                    is_delete[index] = True
            else:
                while min_que and is_delete[min_que[0][1]]:
                    heapq.heappop(min_que)
                
                if min_que:
                    num, index = heapq.heappop(min_que)
                    is_delete[index] = True
    while max_que and is_delete[max_que[0][1]]:
        heapq.heappop(max_que)
          
    while min_que and is_delete[min_que[0][1]]:
        heapq.heappop(min_que)
          
    if not min_que:
        print('EMPTY')
    else:
        print(f"{-max_que[0][0]} {min_que[0][0]}")