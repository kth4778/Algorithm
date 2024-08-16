from itertools import combinations
from collections import deque

def is_fully_connected(coords):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    coord_set = set(tuple(coord) for coord in coords)
    start = tuple(coords[0])
    stack = [start]
    visited = set([start])

    while stack:
        current = stack.pop()
        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if neighbor in coord_set and neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    y_count = 0
    s_count = 0

    if len(visited) == 7:
        for y,x in visited:
            if maps[y][x] == 'S':
                s_count += 1
            else:
                y_count += 1
        if s_count > y_count:
            return True
        return False
    return False
maps = [list(input()) for _ in range(5)]
dx = [1,0,0,-1]
dy = [0,1,-1,0]

count = 0

for i in combinations([[i,j] for i in range(5) for j in range(5)] , 7):
    if is_fully_connected(list(i)):
        count += 1
    
    

print(count)
