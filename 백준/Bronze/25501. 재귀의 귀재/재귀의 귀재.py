t = int(input())

def recursion(s,l,r):
    global count
    count += 1
    if l>=r:
        return 1,count
    elif s[l]!=s[r]:
        return 0,count
    else:
        return recursion(s,l+1,r-1)
for _ in range(t):
    s = input()
    count = 0
    def ispalindrome(s):
        return recursion(s,0,len(s)-1)
    result = ispalindrome(s)
    print(' '.join([str(i) for i in result]))