T = int(input())

for _ in range(T):
    answer = 0

    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = sorted(list(map(int,input().split())))
    
    for i in range(N):
        for j in range(M):
            if A[i] <= B[j]:
                break
            answer += 1

    print(answer)