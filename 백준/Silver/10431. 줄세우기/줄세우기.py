import sys
input = sys.stdin.readline

t = int(input())
answer = [0 for _ in range(t + 1)]

for _ in range(t):
    students = list(map(int,input().split()))

    p = []
    for i in range(1, 21):
        student = students[i]
        p.append(student)
        a = p.index(student)
        p.sort()
        b = p.index(student)

        answer[students[0] - 1] += a - b

for i in range(t):
    print(f"{i + 1} {answer[i]}")
