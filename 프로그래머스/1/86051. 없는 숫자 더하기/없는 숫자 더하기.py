def solution(numbers):
    answer = 0
    
    v = [False for _ in range(10)]
    for i in numbers:
        v[i] = True
    
    for i in range(10):
        if v[i] == False:
            answer += i
    return answer