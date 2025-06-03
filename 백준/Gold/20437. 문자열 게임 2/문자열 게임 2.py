from collections import defaultdict
import sys
input = sys.stdin.readline

def findAnswer(string, r):
    d = defaultdict(list)
    size = len(string)

    minAnswer = size + 1
    maxAnswer = -1

    for i in range(size):
        d[string[i]].append(i)

    for i in d:
        dSize = len(d[i])

        if dSize < K:
            continue

        start = 0
        end = K - 1

        while end < dSize:
            minAnswer = min(minAnswer, d[i][end] - d[i][start] + 1)
            maxAnswer = max(maxAnswer, d[i][end] - d[i][start] + 1)
            start += 1
            end += 1

    return [minAnswer, maxAnswer]

T = int(input())

for _ in range(T):
    W = input().strip()
    K = int(input())

    answer = findAnswer(W,K)

    if answer[1] == -1:
        print(-1)
    else:
        print(*answer)