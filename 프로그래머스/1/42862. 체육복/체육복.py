def solution(n, lost, reserve):
    is_have = {}
    reserve.sort()
    
    for i in range(1, n + 1):
        is_have[i] = True
    
    for i in lost:
        if i not in reserve:
            is_have[i] = False
        
    for i in reserve:
        if i in lost:
            continue
        elif i - 1 > 0 and not is_have[i - 1]:
            is_have[i - 1] = True
        elif i + 1 < n + 1 and not is_have[i + 1]:
            is_have[i + 1] = True
    
    return sum(is_have.values())