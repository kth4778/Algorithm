kda = input().split("/")
k,d,a = [int(i) for i in kda]

if k + a < d or d == 0:
    print("hasu")
else:
    print("gosu")