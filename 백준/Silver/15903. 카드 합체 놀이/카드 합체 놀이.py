import sys
input = sys.stdin.readline

n,m=map(int,input().split())
cards=list(map(int,input().split()))

for _ in range(m):
    cards=[sum(sorted(cards)[:2])]*2+sorted(cards)[2:]
print(sum(cards))