def solution(data, ext, val_ext, sort_by):
    d = {}
    d["code"] = 0
    d["date"] = 1
    d["maximum"] = 2
    d["remain"] = 3
    
    return sorted([i for i in data if i[d[ext]] < val_ext], key = lambda x : x[d[sort_by]])