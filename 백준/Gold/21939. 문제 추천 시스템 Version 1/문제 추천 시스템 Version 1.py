import sys
input = sys.stdin.readline
import heapq

high = []
low = []
question = {}

n = int(input())
for _ in range(n):
    p,l = map(int,input().split())
    heapq.heappush(high, [-l, -p])
    heapq.heappush(low, [l,p])
    question[(p,l)] = True

m = int(input())

for _ in range(m):
    menu = list(input().split())
    if menu[0] == 'add':
        a = int(menu[2])    #난이도
        b = int(menu[1])    #문제 번호
        heapq.heappush(high, [-a,-b])
        heapq.heappush(low, [a, b])
        question[(b,a)] = True
    
    elif menu[0] == 'solved':
        q = int(menu[1])
        for i in question:
            if i[0] == q:
                question[i] = False
                break

    else:
        if menu[1] == '1':
            lst = []
            while True:
                a,b = heapq.heappop(high)   #a: 난이도 b: 문제번호
                lst.append([a,b])
                if question[(-b,-a)]:
                    print(-b)
                    break
            for q,w in lst:
                heapq.heappush(high, [q,w])
            
        else:
            lst = []
            while True:
                a,b = heapq.heappop(low)
                lst.append([a,b])
                if question[(b,a)]:
                    print(b)
                    break
            for q,w in lst:
                heapq.heappush(low, [q,w])