import sys
input = sys.stdin.readline

m,n = map(int,input().split())
bisket = list(map(int,input().split()))

def solution(lst,set_length,num):
    for i in lst:
        if i < set_length:
            continue
        num -= (i // set_length)
        if num <= 0:
            return True
    return False

l = 1
r = max(bisket)

while l <= r:
    mid = (l + r)//2
    p = m
    if solution(bisket[::-1],mid,p):
        l = mid + 1
    else:
        r = mid - 1
print(r)