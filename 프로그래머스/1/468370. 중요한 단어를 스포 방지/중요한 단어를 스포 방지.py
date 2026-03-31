from collections import deque

def solution(message, spoiler_ranges):
    new_spoiler = [False for _ in range(len(message))]
    
    for s, e in spoiler_ranges:
        for i in range(s, e + 1):
            new_spoiler[i] = True
    
    if message[0] == ' ':
        index = 1
    else:
        index = 0
    
    lst = list(message.split())
    
    usageA = {}
    usageB = deque()
    
    for i in lst:
        switch = True
        for j in range(index, index + len(i)):
            if new_spoiler[j]:
                usageB.append(i)
                switch = False
                break
        if switch:
            usageA[i] = True
        index += len(i) + 1
    
    answer = 0
    
    for _ in range(len(usageB)):
        usage = usageB.popleft()
        if usage not in usageA:
            usageA[usage] = True
            answer += 1
    
    return answer
            