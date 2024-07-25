def solution(alpha):
    result = 0
    for i in alpha:
        if i.isdigit():
            result += int(i)
    return result

n = int(input())
lst = [input() for _ in range(n)]
lst.sort()
lst.sort(key= lambda x : (len(x),solution(x)))
for i in lst:
    print(i)