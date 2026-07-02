def solution(s):
    if len(s) == 4 or len(s) == 6:
        if sum([i.isdigit() for i in s]) == len(s):
            return True
        else:
            return False
    else:
        return False