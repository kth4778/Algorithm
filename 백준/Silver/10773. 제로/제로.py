import sys
input = sys.stdin.readline
length=int(input())
stack=[]
for _ in range(length):
    a=int(input())
    if a!=0:
        stack.append(a)
    else:
        stack.pop()
print(sum(stack))