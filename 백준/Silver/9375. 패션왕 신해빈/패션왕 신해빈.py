from itertools import combinations
a=int(input())
for _ in range(a):
    cloth_dict={}
    b=int(input())
    if b==0:
        print(0)
    else:
        for _ in range(b):
            q,w=input().split()
            if w not in cloth_dict:
                cloth_dict[w]=[q]
            else:
                cloth_dict[w].append(q)
        count=0
        for i in cloth_dict:
            if count==0:
                count=len(cloth_dict[i])+1
            else:
                count*=(len(cloth_dict[i])+1)
        print(count-1)