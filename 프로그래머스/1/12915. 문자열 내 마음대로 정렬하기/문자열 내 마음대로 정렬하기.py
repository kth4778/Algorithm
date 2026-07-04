def solution(strings, n):
    return sorted(sorted([s for s in strings]), key = lambda x : x[n])