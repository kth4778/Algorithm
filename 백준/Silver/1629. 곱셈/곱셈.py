def modular_exponentiation(a, b, c):
    result = 1
    a = a % c
    while b > 0:
        if b % 2 == 1: 
            result = (result * a) % c
        b = b >> 1 
        a = (a * a) % c 
    return result
a,b,c=map(int,input().split())

print(modular_exponentiation(a,b,c))