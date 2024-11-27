n = int(input())
lst = sorted(set(list(map(int,input().split()))))

print(*lst)