import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
minimum = float("inf")
s,e = 0, n-1

while s < e:
    new_num = a[s] + a[e]
    
    if abs(new_num) < abs(minimum):
        minimum = new_num

    if new_num < 0:
        s += 1
    elif new_num > 0:
        e -= 1
    else:
        break

print(minimum)