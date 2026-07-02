def solution(n):
    n = sorted([i for i in str(n)], reverse = True)
    answer = ""
    for i in n:
        answer += i
    return int(answer)