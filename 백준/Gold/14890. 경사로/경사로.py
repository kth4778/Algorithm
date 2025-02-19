import sys
input = sys.stdin.readline

N,L = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
count = 0


def solution(lst):
    create_bridge = [False for _ in range(N)]

    height = lst[0]
    index = 0

    while True:
        if index == N - 1:
            break
        
        next_height = lst[index + 1]

        if abs(next_height - height) > 1:
            return False
        
        if next_height == height:
            index += 1
            continue
        
        if abs(next_height - height) == 1:
            if next_height > height:
                for i in range(index, index - L, -1):
                    if 0 > i or N <= i:
                        return False
                    if lst[i] != height:
                        return False
                    if create_bridge[i]:
                        return False
                    
                for i in range(index, index - L, -1):
                    create_bridge[i] = True

            else:
                for i in range(index + 1, index + L + 1):
                    if 0 > i or N <= i:
                        return False
                    if lst[i] != next_height:
                        return False
                    if create_bridge[i]:
                        return False
                for i in range(index + 1, index + L + 1):
                    create_bridge[i] = True
            index + 1
            height = next_height

    return True

for i in range(N):
    lst = []

    if solution(maps[i]):
        count += 1

    for j in range(N):
        lst.append(maps[j][i])
    
    if solution(lst):
        count += 1

print(count)