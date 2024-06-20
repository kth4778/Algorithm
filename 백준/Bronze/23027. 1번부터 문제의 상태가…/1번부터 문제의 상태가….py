a=input()
switch=0
if 'A' in a:
    switch=1
elif 'A' not in a and 'B' in a:
    switch=2
elif 'A' not in a and 'B' not in a and 'C' in a:
    switch=3

if switch==0:
    a='A'*len(a)
elif switch==1:
    a=a.replace('B','A')
    a=a.replace('C','A')
    a=a.replace('D','A')
    a=a.replace('F','A')
elif switch==2:
    a=a.replace('C','B')
    a=a.replace('D','B')
    a=a.replace('F','B')
else:
    a=a.replace('D','C')
    a=a.replace('F','C')
print(a)