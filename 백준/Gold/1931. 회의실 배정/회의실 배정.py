import sys
input = sys.stdin.readline

a=int(input())
result=[list(map(int,input().split())) for _ in range(a)]

result.sort()
result2=sorted(result,key=lambda x:x[1])

studyroom=[]
for i in result2:
    if not studyroom:
        studyroom.append(i)
    else:
        if studyroom[-1][1]<=i[0]:
            studyroom.append(i)
        else:
            pass
print(len(studyroom))
