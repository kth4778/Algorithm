from collections import deque
t=int(input())
for _ in range(t):
    n=int(input())
    triangle=deque([1,1,1,2,2])
    for i in range(n-5):
        triangle.append(triangle[-5]+triangle[-1])

    print(triangle[n-1])