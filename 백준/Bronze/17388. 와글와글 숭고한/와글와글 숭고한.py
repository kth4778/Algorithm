a = ["Soongsil", "Korea", "Hanyang"]

scores = list(map(int,input().split()))

if sum(scores) >= 100:
    print("OK")
else:
    print(a[scores.index(min(scores))])