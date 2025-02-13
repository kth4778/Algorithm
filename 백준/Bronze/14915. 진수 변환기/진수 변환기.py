m,n = map(int,input().split())

numbers = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def solution(m,n):
    answer = ""
    if m > 0:
        while m > 0:
            answer += numbers[m % n]
            m //= n
    else:
        answer = "0"
    
    return answer[::-1]

print(solution(m,n))