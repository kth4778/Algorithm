import sys
input = sys.stdin.readline

a=int(input())
for _ in range(a):
    print(sum(list(map(int,input().split()))))