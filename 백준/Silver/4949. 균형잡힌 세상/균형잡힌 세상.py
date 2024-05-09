def check(i):
    real=[]
    for w in i:
        if  w=='(' or w=='[':
            real.append(w)
        elif w==')':
            if real and real[-1]=='(':
                real.pop()
            else:
                return 'no'
        elif w==']':
            if real and real[-1]=='[':
                real.pop()
            else:
                return 'no'
    else:
        if not real:
            return 'yes'
        else:
            return 'no'
while True:
    a=input()
    if a=='.':
        break
    else:
        print(check(a))