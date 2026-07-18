from collections import deque

def solution(new_id):
    answer = deque()
    
    # 1단계
    for id in new_id:
        answer.append(id.lower())
    # 2단계
    for _ in range(len(answer)):
        s = answer.popleft()
        if s.isalpha() or s.isdigit() or s == "-" or s == "_" or s == ".":
            answer.append(s)
    # 3단계
    before = answer[0]
    
    answer.append(answer.popleft())
    for _ in range(len(answer) - 1):
        s = answer.popleft()
        if before == "." and s == ".":
            continue
        before = s
        answer.append(s)
        
    # 4단계
    if answer and answer[0] == '.':
        answer.popleft()
    if answer and answer[-1] == '.':
        answer.pop()
    # 5단계
    if not answer:
        answer.append('a')
    # 6단계
    if len(answer) >= 16:
        new_answer = deque()
        for _ in range(15):
            new_answer.append(answer.popleft())
        if new_answer[-1] == '.':
            new_answer.pop()
        
        answer = new_answer
    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer = list(answer) + [answer[-1]]
    return ''.join(list(answer))