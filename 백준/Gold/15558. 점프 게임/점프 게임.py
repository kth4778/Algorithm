from collections import deque
import sys
input = sys.stdin.readline


N, K = map(int,input().split())
board = [list(input().strip()) for _ in range(2)]
p = [[0,1,1], [0,1,-1],[-1,-1,K]]

visited = [[False for _ in range(N)] for _ in range(2)]

que = deque()
que.append([0, 0])
visited[0][0] = True
t = -1

while que:
    for _ in range(len(que)):
        direct, cur = que.popleft()
        
        for a,b,c in p:
            newDirect = b * (direct + a)
            nextNode = cur + c
            
            if nextNode < 0:
                continue

            if nextNode >= N:
                print(1)
                sys.exit()

            if nextNode > t + 1 and board[newDirect][nextNode] == "1" and not visited[newDirect][nextNode]:
                visited[newDirect][nextNode] = True
                que.append([newDirect, nextNode])
    
    t += 1


print(0)