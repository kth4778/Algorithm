import sys
input = sys.stdin.readline

result={}
for _ in range(int(input())):
    a=input().strip()
    if a not in result:
        result[a]=1
    else:
        result[a]+=1
max_num=max(result.values())
ret=[i for i in result if result[i]==max_num]
print(sorted(ret)[0])