def solution(participant, completion):
    result = {}
    for i in participant:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    
    for i in completion:
        if result[i] == 1:
            del result[i]
        else:
            result[i] -= 1
    
    return list(result)[0]