def change(num):
    if switchs[num] == 1:
        switchs[num] = 0
    else:
        switchs[num] = 1

n = int(input())
switchs = list(map(int,input().split()))
switchs = [None] + switchs

m = int(input())
for _ in range(m):
    s,num = map(int,input().split())
    
    if s == 1:
        p = num
        while p <= n:
            change(p)
            p += num

    else:
        i = 1
        change(num)
        while True:
            if num - i < 1 or num + i > n:
                break
            if switchs[num - i] == switchs[num + i]:
                change(num - i)
                change(num + i)
                i += 1
            else:
                break

for i in range(1, n + 1):
    print(switchs[i], end = " ")
    if i % 20 == 0:
        print()
                