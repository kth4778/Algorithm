def solution(n, arr1, arr2):
    l = len(arr1)
    maps = [[' ' for _ in range(l)] for _ in range(l)]
    
    for i in range(l):
        for idx, j in enumerate(str(bin(arr1[i])[2:]).zfill(l)):
            if j == '1':
                maps[i][idx] = '#'
    
    for i in range(l):
        for idx, j in enumerate(str(bin(arr2[i])[2:]).zfill(l)):
            if j == '1':
                maps[i][idx] = '#'
    
    return ["".join(i) for i in maps]