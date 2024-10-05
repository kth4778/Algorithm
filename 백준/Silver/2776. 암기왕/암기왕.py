def findNum(num):
    l = 0
    r = N - 1

    while l <= r:
        mid = (l + r) // 2
        p = Nlst[mid]
        if p == num or Nlst[l] == num or Nlst[r] == num:
            return 1 
        elif Nlst[mid] > num:
            r = mid - 1
        else:
            l = mid + 1
    return 0


t = int(input())
for _ in range(t):
    N = int(input())
    Nlst = sorted(list(map(int,input().split())))
    M = int(input())
    Mlst = list(map(int,input().split()))
    for num in Mlst:
        print(findNum(num))