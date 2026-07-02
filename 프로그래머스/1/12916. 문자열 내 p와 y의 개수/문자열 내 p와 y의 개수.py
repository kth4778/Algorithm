def solution(s):
    a = 0
    
    for i in s.lower():
        if i == 'p':
            a += 1
        elif i == 'y':
            a -= 1
    
    return a == 0