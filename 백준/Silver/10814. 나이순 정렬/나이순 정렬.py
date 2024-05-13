a=int(input())
dict={}
for _ in range(a):
    q,w = input().split()
    if q not in dict:
        dict[q]=[]
        dict[q].append(w)
    else:
        dict[q].append(w)

for i in sorted(dict,key=lambda x:int(x)):
    for w in dict[i]:
        print(i,w)