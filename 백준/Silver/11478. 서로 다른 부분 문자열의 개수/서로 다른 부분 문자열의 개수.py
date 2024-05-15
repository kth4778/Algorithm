a=input()
print(len(set([a[i:w+1+i] for i in range(len(a)) for w in range(len(a)-i)])))