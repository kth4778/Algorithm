import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

lst = []
while True:
    try:
        lst.append(int(input()))
    except:
        break

def postorder(lst):
    if len(lst) == 0:
        return 
    mid = lst[0]
    left = []
    right = []
    for i in range(1,len(lst)):
        if lst[i] < mid:
            left.append(lst[i])
        else:
            right.append(lst[i])

    postorder(left)
    postorder(right)

    print(mid)

postorder(lst)