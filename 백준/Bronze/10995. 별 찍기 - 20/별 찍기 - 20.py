n = int(input())
a = "* " * n

for i in range(n):
    if i % 2 == 0:
        print(a)
    else:
        print(" " + a)