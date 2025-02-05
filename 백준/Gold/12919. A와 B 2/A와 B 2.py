A = input()
B = input()

sizeA = len(A)
sizeB = len(B)

def solution(string, size):
    if size == sizeB:
        if string == B:
            print(1)
            exit()
        else:
            return

    case1 = string + "A"
    case2 = (string + "B")[::-1]

    if case1 in B or case1[::-1] in B:
        solution(case1, size + 1)
    
    if case2 in B or case2[::-1] in B:
        solution(case2, size + 1)

solution(A,sizeA)
print(0)