a=list(input().split())
b=[int(a[i][::-1]) for i in range(len(a))]
print(max(b))