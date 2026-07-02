def solution(left, right):
    def c(n):
        p = 0
        for i in range(1, n + 1):
            if n % i == 0:
                p += 1
        return p % 2 == 0
    
    answer = 0
    
    for i in range(left, right + 1):
        if c(i):
            answer += i
        else:
            answer -= i
    
    return answer