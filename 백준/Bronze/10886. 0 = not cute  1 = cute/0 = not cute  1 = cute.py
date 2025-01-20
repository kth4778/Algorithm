N = int(input())
cute = 0
not_cute = 0

for _ in range(N):
    opinion = int(input())
    if opinion:
        cute += 1
    else:
        not_cute += 1
if cute > not_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")