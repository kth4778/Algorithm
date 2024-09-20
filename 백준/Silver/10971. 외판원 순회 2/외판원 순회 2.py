import copy

def solution(city_info, cnt, score, index):
    global answer
    if cnt == n - 1:
        if cities[index][0] == 0:
            return
        answer = min(answer, score + cities[index][0])
        return
    
    for i in range(1,n):
        if not city_info[i] and cities[index][i] != 0:
           copy_city_info = copy.deepcopy(city_info)
           copy_city_info[i] = True
           solution(copy_city_info, cnt + 1, score + cities[index][i], i) 

n = int(input())
cities = [list(map(int,input().split())) for _ in range(n)]
answer = float("INF")

solution({i:False for i in range(n)}, 0, 0, 0)
print(answer)