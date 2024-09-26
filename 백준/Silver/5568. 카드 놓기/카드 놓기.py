from itertools import permutations

def valueOfInteger(num_lst):
    answer = ''
    for num in num_lst:
        answer += str(num)
    return int(answer)

n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]
answer = set()

for i in permutations(cards, k):
    answer.add(valueOfInteger(list(i)))

print(len(answer))