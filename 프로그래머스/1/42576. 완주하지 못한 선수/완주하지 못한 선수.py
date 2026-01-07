def solution(participant, completion):
    d = {}

    for name in participant:
        if name not in d:
            d[name] = 1
        else:
            d[name] += 1
    
    for name in completion:
        if d[name] == 1:
            del d[name]
        else:
            d[name] -= 1
    
    return list(d)[0]