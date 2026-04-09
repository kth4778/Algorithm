answer = -50
lst = list(int(input()) for _ in range(5))
answer += min(lst[:3])
answer += min(lst[3:])
print(answer)