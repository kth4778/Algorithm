import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    phone_numbers = [input().strip() for _ in range(n)]
    phone_numbers.sort()
    for i in range(n-1):
        if phone_numbers[i] == phone_numbers[i+1][:len(phone_numbers[i])]:
            print("NO")
            break
    else:
        print("YES")