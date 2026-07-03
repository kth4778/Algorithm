def solution(n, m):
    answer = []
    
    min_num = min(n, m)
    max_num = max(n, m)
    
    while max_num > 0:
        if n % max_num == 0 and m % max_num == 0:
            answer.append(max_num)
            break
        max_num -= 1
    
    while True:
        if min_num % n == 0 and min_num % m == 0:
            answer.append(min_num)
            break
        min_num += 1
        
    return answer