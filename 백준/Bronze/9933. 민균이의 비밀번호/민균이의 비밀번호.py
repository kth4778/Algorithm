N = int(input())
passwords = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if passwords[i] == passwords[j][::-1]:
            size = len(passwords[i])
            print(f"{size} {passwords[i][size // 2]}")
            exit()