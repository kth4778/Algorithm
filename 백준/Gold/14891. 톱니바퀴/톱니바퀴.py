from collections import deque

def rotation(idx, d, clock_wise, info): #휠인덱스, 좌우, 시계방향, 동서 정보
    global lst

    if idx <= 0 or idx > 4:
        return
    
    if info == wheels[idx][d]:
        return

    lst.append([idx, clock_wise])    

    rotation(idx + d // 2 - 2, d, clock_wise * -1, wheels[idx][-d + 8])

def change_lst(lst,r):
    if r == -1:
        return lst[1:] + [lst[0]]
    else:
        return [lst[-1]] + lst[:7]

wheels =[[]] + [[int(i) for i in list(input())] for _ in range(4)]
k = int(input())
answer = 0

for _ in range(k):
    idx, direction = map(int,input().split())
    lst = [[idx,direction]]
    rotation(idx - 1, 2, direction * -1, wheels[idx][6])
    rotation(idx + 1, 6, direction * -1, wheels[idx][2])
    
    for i,r in lst:
        wheels[i] = change_lst(wheels[i],r)

for i in range(1, 5):
    answer += wheels[i][0] * 2 ** (i - 1) 
    
print(answer)