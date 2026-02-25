S = input()

words = []
index = 0
w = ''

while index < len(S):
    if S[index] == '<':
        if w:
            words.append(w)
            w = ''
        w += '<'
        while True:
            index += 1

            if S[index] == '>':
                w += '>'
                words.append(w)
                w = ''
                index += 1
                break
            else:
                w += S[index]
    
    elif S[index] == ' ':
        words.append(w)
        words.append(' ')
        w = ''
        index += 1
    
    else:
        w += S[index]
        index += 1
if w:
    words.append(w)

result = ''

for i in range(len(words)):
    if words[i][0] == '<':
        result += words[i]
    else:
        result += words[i][::-1]

print(result)