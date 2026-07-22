def solution(n, w, num):
    answer = 0
    c = w
    
    lst = []
    
    for i in range(1, n + 1):
        if c == w:
            c = 0
            lst.append([])
            lst[-1].append(i)
        else:
            lst[-1].append(i)
        c += 1
        
    for i in range(w - len(lst[-1])):
        lst[-1].append(0)
        
    lst = lst[::-1]
    
    for i in range(len(lst)-2, -1, -2):
        lst[i] = lst[i][::-1]
    
    for i in range(len(lst)):
        for j in range(w):
            if lst[i][j] == num:
                dy = i
                dx = j
                while True:
                    answer += 1
                    ny = dy - 1
                    nx = dx
                    if 0 <= ny < len(lst) and 0 <= nx < w:
                        if lst[ny][nx] != 0:
                            dy = ny
                            dx = nx
                        else:
                            break
                    else:
                        break
    return answer
                    
            
    return -1