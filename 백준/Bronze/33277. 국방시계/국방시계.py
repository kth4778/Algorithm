n,m = map(int,input().split())
p = m / n * 1440

print(f"{str(int(p // 60)).zfill(2)}:{str(int(p % 60)).zfill(2)}")