from math import sqrt
n=int(input())
dp=[0,1]
for i in range(2,n+1):
    min_num=4
    for j in range(1,int(sqrt(i))+1):
        min_num=min(min_num,dp[i-j*j])
    dp.append(min_num+1)
print(dp[n])