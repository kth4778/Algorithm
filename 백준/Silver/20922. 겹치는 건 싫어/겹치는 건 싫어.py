import sys
input = sys.stdin .readline

n,k = map(int,input().split())
A = list(map(int,input().split()))
answer = 0
numDict = {}

l,r = 0, 0

while l <= r and 0 <= l < n and 0 <= r < n:
    if A[r] not in numDict:
        numDict[A[r]] = 1
    else:
        numDict[A[r]] += 1

        if numDict[A[r]] > k:
            while A[l] != A[r]:
                numDict[A[l]] -= 1
                l += 1
            l += 1
            numDict[A[r]] -= 1
    
    r += 1

    answer = max(answer, r - l)

print(answer)