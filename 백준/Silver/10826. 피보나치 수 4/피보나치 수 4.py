fib = [0,1]

n = int(input())
if n == 0:
    print(0)
else:
    for _ in range(n - 1):
        fib = [fib[1], fib[0] + fib[1]]

    print(fib[1])