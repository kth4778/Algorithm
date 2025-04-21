x,y = map(int,input().split())
xLst = [0,x]
yLst = [0,y]

t = int(input())

for _ in range(t):
    a,b = map(int,input().split())

    if a == 0:
        yLst.append(b)    
    else:
        xLst.append(b)

xLst.sort()
yLst.sort()

xNewLst = []
yNewLst = []

for i in range(1, len(xLst)):
    xNewLst.append(xLst[i] - xLst[i - 1])

for i in range(1, len(yLst)):
    yNewLst.append(yLst[i] - yLst[i - 1])

answer = 0

for i in xNewLst:
    for j in yNewLst:
        answer = max(answer, i * j)

print(answer)