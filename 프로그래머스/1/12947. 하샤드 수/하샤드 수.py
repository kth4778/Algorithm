def solution(x):
    h = sum([int(i) for i in str(x)])
    return x % h == 0