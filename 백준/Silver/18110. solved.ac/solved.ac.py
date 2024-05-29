import sys
input = sys.stdin.readline

def solution(num):
    a=str(num).split('.')
    if a[1][0]=='5':
        return  int(a[0])+1
    else:
        return round(num)
a=int(input())
if a==0:
    print(0)
else:
    b=sorted([int(input()) for _ in range(a)])
    average=solution(a/10*1.5)
    b=b[average:a-average]
    print(solution(sum(b)/len(b)))