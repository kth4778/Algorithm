def solution(s):
    p = len(s)//2
    if len(s) % 2 == 1:
        return s[p]
    return s[p-1:p+1]