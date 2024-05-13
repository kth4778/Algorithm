import sys
input = sys.stdin.readline

a=int(input())
b=list(map(int,input().split()))

b2=sorted(list(set(b)))
b_dict={b2[i]:i for i in range(len(b2))}

for i in b:
    print(b_dict[i],end=' ')