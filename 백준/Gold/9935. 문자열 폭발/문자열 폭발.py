s = list(input())
bomb = list(input())
bomb_length = len(bomb)
result = []

for i in s:
    result.append(i)
    if len(result) < bomb_length:
        continue
    else:
        if result[-bomb_length:] == bomb:
            del result[-bomb_length:]
if not result:
    print('FRULA')
else:
    print(''.join(result))