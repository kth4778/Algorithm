def solution(keymap, targets):
    answer = []
    
    for i in targets:
        t = 0
        for j in i:
            f = []
            for n in range(len(keymap)):
                if j in keymap[n]:
                    f.append(keymap[n].index(j) + 1)
                
            if not f:
                t = -1
                break
            else:
                t += min(f)
            
        answer.append(t)
    return answer
