import sys
input = sys.stdin.readline

N,S = map(int,input().split())
lst = list(map(int,input().split()))
answer = float("INF")
num = 0

endIndex = 0
startIndex = 0

while endIndex < N:
    num += lst[endIndex]

    while num >= S and startIndex <= endIndex:
        answer = min(answer, endIndex - startIndex + 1)
        num -= lst[startIndex]
        startIndex += 1

    endIndex += 1

if answer == float("INF"):
    print(0)
else:
    print(answer)
