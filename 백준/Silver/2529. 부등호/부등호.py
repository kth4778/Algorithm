n = int(input())
k = list(input().split())

result = []

def solution(num, index):
    global result

    if index == n:
        result.append(num)
        return
    
    for i in range(10):
        if k[index] == "<":
            if int(num[-1]) < i and str(i) not in num:
                solution(num+str(i), index+1)
        else:
            if int(num[-1]) > i and str(i) not in num:
                solution(num+str(i), index+1)

for i in range(10):
    solution(str(i), 0)

result = sorted(result, key = lambda x : int(x))
print(result[-1])
print(result[0])