from collections import deque
def string(lst,bool):
    lst=deque(lst)
    result='['
    if bool:
        while lst:
            result+=','+str(lst.popleft())
        result+=']'
    elif not bool:
        while lst:
            result+=','+str(lst.pop())
        result+=']'
    result=result[0]+result[2:]
    return result
import ast

t=int(input())
for _ in range(t):
    test_case=list(input())
    n=int(input())
    n_lst=ast.literal_eval(input())
    distinc=True
    n_lst=deque(n_lst)

    for i in test_case:
        if i=='D':
            if n_lst and distinc:
                n_lst.popleft()
            elif n_lst and not distinc:
                n_lst.pop()
            elif not n_lst:
                n_lst='error'
                break
        elif i=='R':
            if distinc:
                distinc=False
            else:
                distinc=True
    if n_lst=='error':
        print('error')
    else:
        if not n_lst:
            print('[]')
        else:
            print(string(n_lst,distinc))