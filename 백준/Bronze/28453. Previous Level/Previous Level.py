N = int(input())
M = list(map(int,input().split()))
result = []

for i in M:
    if i == 300:
        result.append('1')
    elif 275 <= i < 300:
        result.append('2')
    elif 250 <= i < 275:
        result.append('3')
    else:
        result.append('4')

print(' '.join(result))