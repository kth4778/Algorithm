def solution(X, Y):
    count_dict = {}
    
    for i in X:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    
    number_lst = []
    
    for i in Y:
        if i in count_dict:
            number_lst.append(i)
            count_dict[i] -= 1
            if count_dict[i] == 0:
                del count_dict[i]
    
    number_lst = sorted(number_lst, reverse = True)
    
    p = ''.join(number_lst)
    
    if not p:
        return "-1"
    
    
    if p[0] == "0":
        return "0"
    
    return p