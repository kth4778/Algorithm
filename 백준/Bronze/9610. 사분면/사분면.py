n = int(input())

a = [None, "Q1: ", "Q2: ", "Q3: ", "Q4: ", "AXIS: "]
b = [0 for _ in range(6)]

for _ in range(n):
    x,y = map(int,input().split())

    if x > 0 and y > 0:
        b[1] += 1
    
    elif x < 0 and y > 0:
        b[2] += 1
    
    elif x < 0 and y < 0:
        b[3] += 1
    
    elif x > 0 and y < 0:
        b[4] += 1
    
    else:
        b[5] += 1

for i in range(1, 6):
    print(a[i] + str(b[i]))