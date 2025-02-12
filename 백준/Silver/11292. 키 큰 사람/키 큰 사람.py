def change_height(h):
    a,b = h.split(".")
    return int(a) * 100 + int(b)

while True:
    n = int(input())
    
    if n == 0:
        exit()

    name = []
    height = []

    for _ in range(n):
        a,b = input().split()
        name.append(a)
        height.append(change_height(b))

    max_height = max(height)

    answer = []

    for i in range(n):
        if height[i] == max_height:
            answer.append(name[i])
    
    print(" ".join(answer))
    
    