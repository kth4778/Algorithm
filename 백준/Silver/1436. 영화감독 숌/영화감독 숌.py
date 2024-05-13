a=int(input())
count=0
s=0
while True:
    if '666' in str(s):
        count+=1
        if count==a:
            print(s)
            break
    s+=1