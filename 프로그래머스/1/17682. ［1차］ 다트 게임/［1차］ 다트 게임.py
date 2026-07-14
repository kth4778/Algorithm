from collections import deque

def solution(dartResult):
    answer = []
    que = deque()
    number = None
    
    for i in dartResult:
        que.append(i)
    
    while que:
        n = que.popleft()
        
        if n.isdigit() and number == None:
            if n == "1":
                q = que.popleft()
                if q == "0":
                    number = 10
                else:
                    number = 1
                    que.appendleft(q)
            else:
                number = int(n)
        elif n.isdigit() and number != None:
            answer.append(number)
            number = None
            que.appendleft(n)
        else:
            if n == "S":
                number **= 1
            elif n == "D":
                number **= 2
            elif n == "T":
                number **= 3
            elif n == "*":
                number *= 2
                if answer:
                    answer[-1] *= 2
            else:
                number *= -1        
    answer.append(number)
    
    return sum(answer)