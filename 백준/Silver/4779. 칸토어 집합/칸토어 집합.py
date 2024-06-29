def divisions(s):
    length = len(s)
    if length == 1:
        return '-'
    else:
        return divisions('-'*(length//3))+' '*(length//3)+divisions('-'*(length//3))
while True:
    try:
        n = int(input())
        print(divisions('-'*(3**n)))
    except:
        exit()