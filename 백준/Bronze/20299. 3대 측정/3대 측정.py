import sys

N, K, L = map(int, sys.stdin.readline().split())

vip_team_count = 0
vip_list = []

for _ in range(N):
    rating_list = list(map(int, sys.stdin.readline().split()))

    condition_1 = all(L <= rating for rating in rating_list)

    if not condition_1:
        continue
    
    condition_2 = K <= sum(rating_list)

    if not condition_2:
        continue
    
    vip_team_count += 1
    vip_list += rating_list

print(vip_team_count)
print(*vip_list)