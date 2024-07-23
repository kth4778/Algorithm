a,b = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
result = list(A - B)
length = len(result)
if length == 0:
    print(0)
else:
    print(length)
    for i in sorted(result):
        print(i,end = ' ')
