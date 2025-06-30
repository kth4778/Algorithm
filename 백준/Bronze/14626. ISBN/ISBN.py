number = input()
s = 0
m = int(number[-1])
index = 0

for i in range(12):
    if number[i] == "*":
        index = i

    else:
        if i % 2 == 0:
            s += int(number[i])
        else:
            s += int(number[i]) * 3

if index % 2 == 0:
    index = 1
else:
    index = 3

if m == 0:
    for i in range(10):
        if (s + i * index) % 10 == 0:
            print(i)

for i in range(10):
    if m == 10 - (s + i * index) % 10:
        print(i)
        exit()