n = int(input())
a = 9
b = 1

result = 0
while True:
    if n < a:
        result += n*b
        break
    else:
        result += a*b
        n -= a
        a *= 10
        b += 1
        
print(result)