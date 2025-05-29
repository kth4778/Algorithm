from collections import deque

def BFS(N,M):
    #거리를 무한대의 값, 큐 생성
    distance = float("INF") 
    queue = deque()

    # 시작 x, y 위치, 이동거리 큐에 넣고 방문 배열 표시
    queue.append([0,0,1])
    visited[0][0] = True
    
    while queue:
        # 현재 y위치, x위치, 이동거리
        y,x,move = queue.popleft()

        if y == N - 1 and x == M - 1:
            #목적지 최소 이동거리 갱신후 다음 정점 꺼내기
            distance = min(distance, move)
            continue
        
        #좌,우,상,하 검사
        for i in range(4):   
            ny, nx = y + dy[i], x + dx[i]

            # 방문 할 위치가 미로 밖을 벗어나는지 검사
            if 0 <= ny < N and 0 <= nx < M: 
                # 만약 방문하지 않았고 벽이 아니면 방문처리후, 
                # 큐에 이동거리 + 1 해서 추가
                if not visited[ny][nx] and maze[ny][nx] != 0:
                    visited[ny][nx] = True
                    queue.append([ny, nx, move + 1])
    
    return distance

N,M = map(int,input().split())    #세로, 가로 입력받음
maze = [list(map(int, input().strip())) for _ in range(N)]
# 세로열의 개수 만큼 미로 입력받음

visited = [[False for _ in range(M)] for _ in range(N)]
# 방문 배열을 가로 세로 넓이만큼 만듦

dy = [0,0,-1,1]
dx = [-1,1,0,0]
#좌, 우, 상, 하

answer = BFS(N,M)
print(answer)