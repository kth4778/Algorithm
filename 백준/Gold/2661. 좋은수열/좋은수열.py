N = int(input())

def solution(num, size):
    if size == N:
        print(num)
        exit()
    
    for i in range(1, 4):
        new_num = num + str(i)
        s = len(new_num)
        switch = True

        for j in range(1, s // 2 + 1):
            if new_num[-j:] == new_num[-(j * 2):-j]:
                switch = False
                break
        
        if switch:
            solution(new_num, size + 1)

solution("", 0)