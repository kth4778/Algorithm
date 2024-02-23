num=[int(input()) for i in range(10)]
num1=[y%42 for y in num]
print(len(set(num1)))