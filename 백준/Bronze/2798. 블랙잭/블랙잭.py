from itertools import combinations
N,M=map(int,input().split())
cards_list=list(map(int,input().split()))
a=[]
comb_list=[sum(i) for i in list(combinations(cards_list,3)) if sum(i)<=M]
print(sorted(comb_list)[-1])