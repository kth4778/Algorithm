import sys
input = sys.stdin.readline

numbers = []
p = list(map(int,input().split()))
size = p[0]

size -= len(p[1:])

for i in p[1:]:
    numbers.append(int(str(i)[::-1]))

while size > 0:
    p = list(map(int,input().split()))
    size -= len(p)

    for i in p:
        numbers.append(int(str(i)[::-1]))

for i in sorted(numbers):
    print(i)