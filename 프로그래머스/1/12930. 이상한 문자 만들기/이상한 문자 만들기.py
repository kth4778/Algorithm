def solution(s):
    result = ""
    idx = 0
    
    for i in range(len(s)):
        if s[i] != " ":
            if idx % 2 == 0:
                result += s[i].upper()
            else:
                result += s[i].lower()
            idx += 1
        else:
            idx = 0
            result += " "
    return result