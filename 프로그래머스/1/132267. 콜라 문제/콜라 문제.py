def solution(a, b, n):
    result = 0

    while n >= a:
        r = (n // a) * b
        n = n % a
        n += r
        result += r
        print(r)
        
    return result