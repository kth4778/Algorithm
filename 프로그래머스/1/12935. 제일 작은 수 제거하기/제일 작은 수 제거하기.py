def solution(arr):
    a = min(arr)
    
    answer = []
    for i in arr:
        if i != a:
            answer.append(i)
    
    if not answer:
        return [-1]
    return answer