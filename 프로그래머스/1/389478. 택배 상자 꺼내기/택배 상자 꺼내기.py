def solution(n,w,num):
    lst = [[None for _ in range(w)] for _ in range(n // w + 1)]
    number = 1
    floor = 0
    switch = False
    
    while number <= n:
        if not switch:
            for i in range(w):
                if number > n:
                    break
                lst[floor][i] = number
                number += 1
        else:
            for i in range(w - 1, -1, -1):
                if number > n:
                    break
                lst[floor][i] = number
                number += 1
        floor += 1
        switch = not switch
    
    y, x = 0, 0
    p = False
    
    for i in range(n // w + 1):
        for j in range(w):
            if lst[i][j] == num:
                y, x = i, j
                p = True
                break
        if p:
            break
    count = 0
    
    for i in range(y, n // w + 1):
        if lst[i][x] != None:
            count += 1
        else:
            break
    
    
    return count