result=[]
def solution(s):
    if s.startswith('pop'):
        if result:
            return result.pop()
        else:
            return -1
    elif s.startswith('size'):
        return len(result)
    elif s.startswith('empty'):
        if not result:
            return 1
        else:
            return 0
    else:
        if result:
            return result[-1]
        else:
            return -1

a=int(input())
b=[input() for _ in range(a)]

for i in b:
    if i.startswith('push'):
        result.append(i.split()[1])
    else:
        print(solution(i))