def solution(s, n):
    answer = ''
    
    for i in s:
        p = ord(i) + n
        if i.islower():
            if p > 122:
                answer += chr(97 + p % 123)
            else:
                answer += chr(p)
        elif i.isupper():    
            if p > 90:
                answer += chr(65 + p % 91)
            else:
                answer += chr(p)
        else:
            answer += i
            
    return answer


# 65 ~ 90, 97 ~ 122