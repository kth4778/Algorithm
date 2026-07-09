def solution(k, m, score):
    result = 0
    index = len(score)
    score.sort()
    
    for _ in range(len(score) // m):
        result += m * (min(score[index - m:index]))
        index -= m
    
    return result