n = int(input())
answer = 0

for i in range(n):
    for j in range(n):
        if i != j:
            answer += 1

print(answer)