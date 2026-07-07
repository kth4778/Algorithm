def solution(name, yearning, photo):
    l = len(name)
    answer = [0 for _ in range(len(photo))]
    name_dict = {}
    
    for i in range(l):
        name_dict[name[i]] = yearning[i]
    
    for idx, i in enumerate(photo):
        for j in range(len(i)):
            if i[j] in name_dict:
                answer[idx] += name_dict[i[j]]
    
    return answer
    
    