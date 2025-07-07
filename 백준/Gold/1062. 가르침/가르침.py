from itertools import combinations

N,K = map(int,input().split())
words = [input() for _ in range(N)]
newWord = ['b', 'd', 'e', 'f', 'g',
        'h', 'j', 'k', 'l', 'm',
        'o', 'p', 'q', 'r', 's', 
        'u', 'v', 'w', 'x', 'y', 'z']
answer = 0

if K < 5:
    print(0)
    exit()

for i in combinations(newWord, K - 5):
    setWord = {'a': True, 'c': True, 'i': True, 'n': True, 't': True, 'b': False, 'd': False, 'e': False, 'f': False, 'g': False, 'h': False, 'j': False, 'k': False, 'l': False, 'm': False, 'o': False, 'p': False, 'q': False, 'r': False, 's': False, 'u': False, 'v': False, 'w': False, 'x': False, 'y': False, 'z': False}

    for j in i:
        setWord[j] = True

    count = 0

    for word in words:
        switch = True
        for q in word:
            if setWord[q] == False:
                switch = False
                break
        if switch:
            count += 1

    answer = max(answer, count)

print(answer)