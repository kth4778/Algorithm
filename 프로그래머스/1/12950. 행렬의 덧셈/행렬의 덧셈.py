def solution(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr1[0])
    
    arr = [[None for _ in range(len2)] for _ in range (len1)]
    
    for i in range(len1):
        for j in range(len2):
            arr[i][j] = arr1[i][j] + arr2[i][j] 
    
    return arr