alphabats = input()
target = input()
n1 = len(alphabats)
n2 = len(target)
index = 0
answer = 0

while index < n1:
    if alphabats[index : index + n2] != target:
        index += 1
    elif alphabats[index : index + n2] == target:
        answer += 1
        index += n2

print(answer)