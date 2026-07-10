def solution(N, stages):
    stages.sort()
    stage_dict = {}
    l = len(stages)
    
    for i in range(1, N + 1):
        if i in stages:
            stage_dict[i] = stages.count(i) / (l - stages.index(i))
        else:
            stage_dict[i] = 0
    
    stage_dict = sorted(stage_dict.items(), key=lambda x : x[1], reverse = True)
    return [i[0] for i in stage_dict]

