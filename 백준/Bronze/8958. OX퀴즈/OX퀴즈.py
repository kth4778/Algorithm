def factorial(num):
    a=0
    for i in range(1,num+1):
        a+=i
    return a


a=int(input())
for _ in range(a):
    a=input().split('X')
    print(sum([factorial(i.count('O')) for i in a]))