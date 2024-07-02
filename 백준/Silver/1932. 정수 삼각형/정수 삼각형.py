a = int(input())
triangle = [list(map(int,input().split())) for _ in range(a)]

t = 1
while t<a:
    for i in range(len(triangle[t])):
        if i == 0:
            triangle[t][i] += triangle[t-1][0]
        elif i == len(triangle[t])-1:
            triangle[t][i] += triangle[t-1][-1]
        else:
            triangle[t][i] += max(triangle[t-1][i-1],triangle[t-1][i])
    t += 1
print(max(triangle[-1]))