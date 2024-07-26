n,m = map(int,input().split())
lst = list(map(int,input().split()))
l = 0
r = 0
result = 0
num = 0

lst = [0] + lst
while l <= n:
    r += 1
    if r > n:
        break
    num += lst[r]
    if num > m :
        l += 1
        r = l
        num = 0
    elif num == m:
        l += 1
        r = l   
        result += 1
        num = 0
print(result)