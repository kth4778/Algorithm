n = int(input())
students = [list(input().split()) for _ in range(n)]
students.sort()
students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3])))
for i in [j[0] for j in students]:
    print(i)