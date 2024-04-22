n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
test_b=b[:]
print(sum([a*b for a,b in zip(sorted(a,reverse=True),sorted(test_b))]))
