import sys
sys.setrecursionlimit(10 ** 5)

t = int(input())

for _ in range(t):
    n = int(input())
    students = [0] + list(map(int,input().split()))
    count = 0
    visited = [False for _ in range(n + 1)]

    def dfs(i):
        global count

        visited[i] = True
        cycle_list.append(i)

        next_node = students[i]

        if visited[next_node]:    
            if next_node in cycle_list:
                count += len(cycle_list[cycle_list.index(next_node):])
        else:
            dfs(next_node)

    for i in range(1, n + 1):
        if not visited[i]:
            cycle_list = []
            dfs(i)
    
    print(n - count)