n = int(input())
answer = ["no", "yes"]
print(answer[int(sum(list(map(int,input().split()))) % 3 == 0)])