A,P = map(int,input().split())

def change(num):
    result = 0
    for i in str(num):
        result += int(i) ** P
    return result

que = [A]

while True:
    change_num = change(que[-1])
    if change_num in que:
        print(que.index(change_num))    
        break
    
    que.append(change_num)