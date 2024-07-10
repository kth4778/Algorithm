n = int(input())
profit = list(map(int,input().split()))
price = list(map(int,input().split()))
lst = [profit[i]-price[i] for i in range(n)]
p = sorted(profit)
max_cost = p[-1]
sub_cost = p[-2]

max_profit = max(profit)

for i in range(n):
    if profit[i] == max_profit:
        print(profit[i] - (sub_cost-price[i]) - price[i], end = ' ')
    else:
        print(profit[i] - (max_cost - price[i]) - price[i], end = ' ' )             