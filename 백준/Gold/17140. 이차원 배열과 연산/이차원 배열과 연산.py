from collections import Counter
import sys
input = sys.stdin.readline

y,x,k = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(3)]
count = 0

def chage_arr(lst):
    c = [[num, cnt] for num, cnt in Counter(lst).items() if num != 0]
    c.sort(key = lambda x : (x[1],x[0]))
    
    result = []

    for i in c:
        for j in i:
            result.append(j)
    return result, len(result)

while True:
    c_size = len(maps[0]) #열 개수
    r_size = len(maps)    #행 개수

    try:
        if maps[y - 1][x - 1] == k:
            break
    except:
        pass

    if count == 100:
        count = -1
        break

    new_maps = []
    max_size = 0

    if r_size >= c_size:
        for i in maps:
            lst, size = chage_arr(i)
            new_maps.append(lst)
            max_size = max(max_size, size)

        for i in range(len(new_maps)):
            new_maps[i] = new_maps[i] + [0] * (max_size - len(new_maps[i]))
        
        maps = new_maps

    else:
        for j in range(c_size):
            p = []
            for i in range(r_size):
                p.append(maps[i][j])
            
            lst, size = chage_arr(p)
            new_maps.append(lst)
            max_size = max(max_size, size)

        q = [[0 for _ in range(len(new_maps))] for _ in range(max_size)]

        for j in range(len(new_maps)):
            for i in range(len(new_maps[j])):
                q[i][j] = new_maps[j][i]

        maps = q            

    count += 1

print(count)