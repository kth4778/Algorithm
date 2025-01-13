S = input()

m = ['a','e','i','o','u']
answer = ""
index = 0

while index < len(S):
    if S[index] in m:
        answer += S[index]
        index += 2
    else:
        answer += S[index]
    index += 1

print(answer)