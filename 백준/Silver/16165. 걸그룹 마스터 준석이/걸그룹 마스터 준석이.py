import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dic1 = {}
dic0 = {}
for _ in range(n):
    girl_group_name = input().strip()
    dic0[girl_group_name] = []
    t = int(input())
    for _ in range(t):
        girl_name = input().strip()
        dic1[girl_name] = girl_group_name
        dic0[girl_group_name].append(girl_name)
for i in dic0:
    dic0[i].sort()

for _ in range(m):
    s = input().strip()
    p = int(input())
    if p == 0:
        for name in dic0[s]:
            print(name)
    else:
        print(dic1[s])