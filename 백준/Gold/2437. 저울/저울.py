import sys
input = sys.stdin.readline

a = int(input())
b = list(map(int, input().split()))

b.sort()  # 오름차순 정렬

smallest_missing = 1

for num in b:
    if num > smallest_missing:
        break
    smallest_missing += num

print(smallest_missing)
