e,s,m = map(int,input().split())

se,ss,sm = 1,1,1
cnt = 1

while True:
    if se == e and ss == s and sm == m:
        break
    if se + 1 == 16:
        se = 1
    else:
        se += 1
    
    if ss + 1 == 29:
        ss = 1
    else:
        ss += 1
    
    if sm + 1 == 20:
        sm = 1
    else:
        sm += 1
    
    cnt += 1

print(cnt)