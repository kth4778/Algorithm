def solution(d, budget):
    result = 0
    
    for i in sorted(d):
        if budget - i < 0:
            return result
        result += 1
        budget -= i
    
    return result