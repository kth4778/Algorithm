n,score,p = map(int,input().split())

if n == 0:
    print(1)
    exit()

scores = list(map(int,input().split()))
scores.append(score)
scores.sort(reverse=True)

index = scores.index(score)
count = scores.count(score)

result = -1

if index + count <= p:
    result = index + 1

print(result)