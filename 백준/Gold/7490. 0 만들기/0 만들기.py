def calcul(s):
    p = 0
    switch = 1
    set_num = 0

    for i in range(len(s)):
        if i % 2 == 0:
            set_num += int(s[i])
        else:
            if s[i] == "-":
                p += switch * set_num
                set_num = 0
                switch = -1
            elif s[i] == "+":
                p += switch * set_num
                set_num = 0
                switch = 1
            else:
                set_num *= 10
    p += switch * set_num
    return p
                

def solution(s, q, nxn):
    if len(s) == n * 2 - 1:
        if calcul(s) == 0:
            print(s)
            return
    else:
        if q == 1:
            for i in range(3):
                solution(s + b[i], 0, nxn)
        else:
            solution(s + str(nxn), 1, nxn + 1)



t = int(input())
b = [" ", "+", "-"]

for _ in range(t):
    n = int(input())
    solution("", 0, 1)
    print()