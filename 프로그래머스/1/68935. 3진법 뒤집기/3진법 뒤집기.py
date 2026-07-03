def solution(n):
    s = ""
    result = 0
    
    while n > 0:
        s += str(n % 3)
        n //= 3
    
    s = str(int(s))[::-1]
    
    for i in range(len(s)):
        result += int(s[i]) * (3 ** i)
    
    return result