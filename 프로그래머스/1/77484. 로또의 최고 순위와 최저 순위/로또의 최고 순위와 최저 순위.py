def solution(lottos, win_nums):
    q = 0
    w = 0
    
    for i in lottos:
        if i in win_nums:
            q += 1
            w += 1
        elif i == 0:
            w += 1
    
    lottos_dict = {}
    lottos_dict[6] = 1
    lottos_dict[5] = 2
    lottos_dict[4] = 3
    lottos_dict[3] = 4
    lottos_dict[2] = 5
    lottos_dict[1] = 6
    lottos_dict[0] = 6
    
    return [lottos_dict[w], lottos_dict[q]]
    