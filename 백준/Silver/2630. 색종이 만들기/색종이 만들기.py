n=int(input())
paper=[list(map(int,input().split())) for _ in range(n)]

result=[]

def solution(y,x,n):
    color=paper[y][x]
    for i in range(y,y+n):
        for w in range(x,x+n):
            if paper[i][w]!=color:
                solution(y,x,n//2)
                solution(y+n//2,x,n//2)
                solution(y,x+n//2,n//2)
                solution(y+n//2,x+n//2,n//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0,0,n)
print(result.count(0))
print(result.count(1))