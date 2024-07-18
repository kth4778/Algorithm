from itertools import combinations

l,c = map(int,input().split())

def check(s):
    alpha = ['a','e','i','o','u']
    cnt1 = 0
    cnt2 = 0

    for i in s:
        if i in alpha:
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 >= 1 and cnt2 >= 2:
        return True
    return False


alphabat_lst = list(input().split())
alphabat_lst.sort()
for i in combinations(alphabat_lst,l):
    if check(i):
        print(''.join(list(i)))