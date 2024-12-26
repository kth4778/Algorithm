n = int(input())
a_score = 0
b_score = 0

for i in input():
    if i == 'A':
        a_score += 1
    else:
        b_score += 1
if a_score > b_score:
    print('A')
elif b_score > a_score:
    print('B')
else:
    print('Tie')