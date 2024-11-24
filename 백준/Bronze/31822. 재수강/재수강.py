p = input()
N = int(input())
answer = 0
set_code = p[:5]

for _ in range(N):
    s = input()
    if s[:5] == set_code:
        answer += 1

print(answer)