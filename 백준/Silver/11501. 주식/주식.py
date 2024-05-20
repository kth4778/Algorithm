import sys
input = sys.stdin.readline

def solution(lst,length):
    max_price=0
    profit_money=0

    for i in range(length-1,-1,-1):
        if lst[i]>max_price:
            max_price=lst[i]
        profit_money+=max_price-lst[i]
    return profit_money

a=int(input())
for _ in range(a):
    p=int(input())
    o=list(map(int,input().split()))
    print(solution(o,p))