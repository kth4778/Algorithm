import sys
input = sys.stdin.readline

def change_coordinate(y,x):
    if x == -1:
        x = m - 1
    elif x == m:
        x = 0
    
    if y == -1:
        y = n - 1
    elif y == n:
        y = 0
    
    return y,x

def add_word(y,x, count, word):
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

    if count > max_word_length:
        return
    
    for i in range(8):
        ny, nx = change_coordinate(y + dy[i], x + dx[i])
        add_word(ny, nx, count + 1, word + maps[ny][nx])


n,m,k = map(int,input().split())
words = {}
maps = [list(input().strip()) for _ in range(n)] 
requestWords = []
max_word_length = -1

dy = [0,0,1,-1,1,-1,1,-1]
dx = [1,-1,0,0,-1,-1,1,1]

for _ in range(k):
    word = input().strip()
    requestWords.append(word)
    max_word_length = max(max_word_length, len(word))


for y in range(n):
    for x in range(m):
        add_word(y,x,1,maps[y][x])

for word in requestWords:
    if word not in words:
        print(0)
    else:
        print(words[word])
