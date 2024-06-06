num=0
a=[input() for _ in range(3)]
for i in range(3):
    if a[i].isdigit():
        num=int(a[i])+(3-i)
        break
if num%3==0 and num%5==0:
    print('FizzBuzz')
elif num%3==0 and num%5!=0:
    print('Fizz')
elif num%3!=0 and num%5==0:
    print('Buzz')
else:
    print(num)