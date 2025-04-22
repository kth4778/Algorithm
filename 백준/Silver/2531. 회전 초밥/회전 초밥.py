import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
rice = []
answer = 0

for _ in range(n):
    rice.append(int(input()))

def solution(index):
    p = set()

    for i in range(index, index + k):
        p.add(rice[i % n])
    
    p.add(c)
    
    return len(p)

for i in range(n):
    answer = max(answer, solution(i))

print(answer)