def solution(s):
    d = {}
    result = []
    
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = i
            result.append(-1)
        else:
            result.append(i - d[s[i]])
            d[s[i]] = i
    return result