def solution(s):
    return "".join(sorted([i for i in s], key = lambda x : ord(x), reverse = True))