a=[input() for i in range(5)]
max_nums=max((len(i) for i in a))
op=[]
for i in range(max_nums):
    for w in a:
        if i<len(w):
            op.append(w[i])
print(''.join(op))