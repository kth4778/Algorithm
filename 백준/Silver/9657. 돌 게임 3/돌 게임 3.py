n = int(input())
dp = [False for _ in range(n + 1)]
m = [1,3,4]

for i in m:
    if i <= n:
        dp[i] = True

for i in range(n + 1):
    switch = False
    for j in m:
        if i - j > 0:
            if not dp[i - j]:
                switch = True
                break
    
    if switch:
        dp[i] = True

if not dp[n]:
    print("CY")
else:
    print("SK")