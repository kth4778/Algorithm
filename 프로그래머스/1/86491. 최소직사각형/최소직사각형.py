def solution(sizes):
    l = len(sizes)
    
    for i in range(l):
        sizes[i].sort()
        
    return max([sizes[i][0] for i in range(l)]) * max([sizes[i][1] for i in range(l)])