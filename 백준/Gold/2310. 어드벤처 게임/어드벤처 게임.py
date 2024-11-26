from collections import deque
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        sys.exit()
    else:
        node_info = [[None]]
        distance = {i:-1 for i in range(1, n + 1)}
        que = deque()
        switch = True

        for _ in range(n):
            p = list(input().split())
            node_info.append([p[0],int(p[1]),[int(i) for i in p[2:-1]]])
        
        
        if node_info[1][0] == "E":
            distance[1] = 0
            que.append([1,0])
        elif node_info[1][0] == "L":
            distance[1] = node_info[1][1]
            que.append([1,node_info[1][1]])
        else:
            print('No')
            continue
        
        while que:
            cur, cost = que.popleft()
            if cur == n:
                switch = False
                break

            for next_node in node_info[cur][2]:
                next_cost = node_info[next_node][1]
                money = None

                if node_info[next_node][0] == 'T':
                    if cost < next_cost:
                        continue
                    money = cost - next_cost

                elif node_info[next_node][0] == 'L':
                    money = max(cost, next_cost)
                
                else:
                    money = cost
                
                if distance[next_node] < money:
                    distance[next_node] = money
                    que.append([next_node, money])

        if switch:
            print('No')
        else:
            print('Yes')