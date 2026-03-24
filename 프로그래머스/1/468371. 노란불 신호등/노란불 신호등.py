from collections import deque

def solution(signals):
    size = len(signals)
    colors = ['green', 'yellow', 'red']
    
    que = deque()
    color_table = [[] for _ in range(size)]
    
    for i in range(size):
        que.append([0, i])
        for j in range(3):
            for k in range(signals[i][j]):
                color_table[i].append(colors[j])
    
    G = 0
    Y = 0
    R = 0
    
    while que:    
        time, index = que.popleft()
        if time == 20 ** 5:
            return -1
        
        color = color_table[index][time % sum(signals[index])]

        if color == 'green':
            G += 1
        elif color == 'yellow':
            Y += 1
        else:
            R += 1
        
        que.append([time + 1, index])
        
        if index == size - 1:
            if Y == size:
                return time + 1
            else:        
                G = 0
                Y = 0
                R = 0