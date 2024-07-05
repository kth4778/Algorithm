n = int(input())
c = input()

result = 1
idx = 0
while idx<n:
    if c[idx] == 'S':
        result += 1
        idx += 1
    else:
        result += 1
        idx += 2
print(min(result,n))