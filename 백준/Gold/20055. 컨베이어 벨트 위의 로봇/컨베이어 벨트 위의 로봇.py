N,K = map(int,input().split())
A = list(map(int,input().split()))

robot = [False for _ in range(N)]
level = 1

while True:
    A = [A[-1]] + A[:-1]
    robot = [False] + robot[:-1]
    
    if robot[N - 1]:
        robot[N - 1] = False
        
    for i in range(N - 2, -1, -1):
        if robot[i] and A[i + 1] > 0 and not robot[i + 1]:
            A[i + 1] -= 1
            robot[i] = False
            robot[i + 1] = True
    robot[N - 1] = False

    if A[0] > 0 and not robot[0]:
        robot[0] = True
        A[0] -= 1

    if A.count(0) >= K:
        break

    level += 1


print(level)