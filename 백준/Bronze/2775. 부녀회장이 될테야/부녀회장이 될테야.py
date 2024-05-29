a=int(input())
for _ in range(a):
    q=int(input())
    w=int(input())
    result=[i for i in range(1,w+1)]
    for _ in range(q):
        for i in range(w):
            result.append(sum(result[:i+1]))
        result=result[w:]
    print(result[-1])

