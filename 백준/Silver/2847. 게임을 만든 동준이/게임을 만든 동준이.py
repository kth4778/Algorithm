import sys
input = sys.stdin.readline

level_score=[]
drop_score=0
a=int(input())

for _ in range(a):
    level_score.append(int(input()))

level_score2=level_score[::-1]
result=[level_score2[0]]

for i in level_score2[1:]:
    if i>=result[-1]:
        drop_score+=(i-result[-1]+1)
        result.append(result[-1]-1)
    else:
        result.append(i)
print(drop_score)