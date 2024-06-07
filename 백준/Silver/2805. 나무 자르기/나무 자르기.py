import sys
input = sys.stdin.readline

n,m=map(int,input().split())
tree=list(map(int,input().split()))

def solution(tree,num):
    count=0
    for i in tree:
        if i-num>0:
            count+=i-num
    return count

def bin_search(tree,m):
    pl=0
    pr=max(tree)
    while pr>=pl:
        pc = (pl+pr)//2
        if solution(tree,pc)<m:
            pr=pc-1
        else:
            pl=pc+1
    return pr
print(bin_search(tree,m))