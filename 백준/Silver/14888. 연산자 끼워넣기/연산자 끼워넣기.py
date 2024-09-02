import sys
import copy
from collections import deque

# sys.setrecursionlimit(10 ** 6)

def bfs(lst, index, p):
    # print(f"lst: {lst}, index: {index}, p: {p}")
    # print('-----------------------------------')
    if index == n:
        global min_answer
        global max_answer
        min_answer = min(min_answer,p)
        max_answer = max(max_answer, p)
    else:
        for i in range(4):
            if lst[i] > 0:
                if i == 0:
                    lst1 = copy.deepcopy(lst)
                    lst1[0] -= 1
                    bfs(lst1, index + 1, a_lst[index] + p)
                elif i == 1:
                    lst2 = copy.deepcopy(lst)
                    lst2[1] -= 1
                    bfs(lst2, index + 1, p - a_lst[index])
                elif i == 2:
                    lst3 = copy.deepcopy(lst)
                    lst3[2] -= 1
                    bfs(lst3, index + 1, p * a_lst[index])
                elif i == 3:
                    lst4 = copy.deepcopy(lst)
                    lst4[3] -= 1
                    if p < 0 and a_lst[index] >= 0:
                        bfs(lst4, index + 1, - (-p // a_lst[index]))
                    else:
                        bfs(lst4, index + 1, p // a_lst[index])

n = int(input())
a_lst = list(map(int,input().split()))
modify = list(map(int,input().split()))

que = deque()
min_answer = float("INF")
max_answer = -float("INF")

bfs(modify, 1, a_lst[0])
print(max_answer)
print(min_answer)