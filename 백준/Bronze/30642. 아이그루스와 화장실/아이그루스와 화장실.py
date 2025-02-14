n = int(input())
name = input()
k = int(input())

if name == "annyong":
    if k % 2 != 0:
        print(k)
    else:
        for i in [k - 1, k + 1]:
            if 1 <= i <= n:
                print(i)
                break
else:
    if k % 2 == 0:
        print(k)
    else:
        for i in [k - 1, k + 1]:
            if 1 <= i <= n:
                print(i)
                break