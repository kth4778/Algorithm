import sys
input = sys.stdin.readline

p = ['a','e','i','o','u']
    

def case1(password):
    for i in password:
        if i in p:
            return True
    
    return False

def case2(password):
    dic = {chr(i):"자음" for i in range(97, 123)}
    for i in p:
        dic[i] = "모음"

    count = 0
    word = None

    for i in password:
        if dic[i] != word:
            count = 1
            word = dic[i]
        else:
            count += 1
        
        if count == 3:
            return False
    
    return True

def case3(password):
    word = None

    for i in password:
        if word == i:
            if i == 'e' or i == 'o':
                continue
            else:
                return False
        
        word = i

    return True

while True:
    password = input().strip()
    
    if password == "end":
        sys.exit()

    if case1(password) and case2(password) and case3(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
    