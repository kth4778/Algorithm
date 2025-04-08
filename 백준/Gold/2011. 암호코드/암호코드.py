n = input()
size = len(n)
dp = [0 for _ in range(size + 1)]
dp[0], dp[1] = 1,1

if n[0] == "0":
    print(0)
    exit()

if size == 1:
    print(1)
    exit()

for i in range(2, size):
    pre, cur, nxt = int(n[i - 2]), int(n[i - 1]), int(n[i])

    if cur == 0:
        if pre > 2 or nxt == 0:
            print(0)
            exit()
        else:
            dp[i] = dp[i - 1]
        
    else:
        if nxt != 0 and pre * 10 + cur < 27 and pre != 0:
            dp[i] = dp[i - 1] + dp[i - 2]
        else:
            dp[i] = dp[i - 1]

if n[size - 1] == "0":
    if int(n[size - 2]) > 2:
        print(0)
        exit()
    else:
        dp[size] = dp[size - 1]
else:
    if n[size - 2] == "0" or int(n[size - 2]) * 10 + int(n[size - 1]) > 26:
        dp[size] = dp[size - 1]
    else:
        dp[size] = dp[size - 1] + dp[size - 2]

print(dp[size] % 1000000)